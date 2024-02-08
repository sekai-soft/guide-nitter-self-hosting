# adapted from
# https://github.com/zedeus/nitter/issues/983#issuecomment-1914616663
import requests
import base64
import getpass
import json

username = input("Twitter username: ")
password = getpass.getpass("Twitter password: ")

TW_CONSUMER_KEY = '3nVuSoBZnx6U4vzUxf5w'
TW_CONSUMER_SECRET = 'Bcs59EFbbsdF6Sl9Ng71smgStWEGwXXKSjYvPVt7qys'
TW_ANDROID_BASIC_TOKEN = 'Basic {token}'.format(token=base64.b64encode(
    (TW_CONSUMER_KEY + ":" + TW_CONSUMER_SECRET).encode()
).decode())
print("TW_ANDROID_BASIC_TOKEN=" + TW_ANDROID_BASIC_TOKEN)

authentication = None
bearer_token_req = requests.post("https://api.twitter.com/oauth2/token",
	headers={
      'Authorization': TW_ANDROID_BASIC_TOKEN,
      "Content-Type": "application/x-www-form-urlencoded",
    },
	data='grant_type=client_credentials'
).json()
bearer_token = ' '.join(str(x) for x in bearer_token_req.values())
print("bearer_token=" + bearer_token)

# The bearer token is immutable
# Bearer AAAAAAAAAAAAAAAAAAAAAFXzAwAAAAAAMHCxpeSDG1gLNLghVe8d74hl6k4%3DRUMF4xAQLsbeBhTSRrCiQpJtxoGWeyHrDb5te2jpGskWDFW82F
guest_token = requests.post("https://api.twitter.com/1.1/guest/activate.json", headers={
	'Authorization': bearer_token,
}).json()['guest_token']
print("guest_token=" + guest_token)

twitter_header = {
    'Authorization': bearer_token,
    "Content-Type": "application/json",
    "User-Agent":
        "TwitterAndroid/9.95.0-release.0 (29950000-r-0) ONEPLUS+A3010/9 (OnePlus;ONEPLUS+A3010;OnePlus;OnePlus3;0;;1;2016)",
    "X-Twitter-API-Version": '5',
    "X-Twitter-Client": "TwitterAndroid",
    "X-Twitter-Client-Version": "9.95.0-release.0",
    "OS-Version": "28",
    "System-User-Agent":
        "Dalvik/2.1.0 (Linux; U; Android 9; ONEPLUS A3010 Build/PKQ1.181203.001)",
    "X-Twitter-Active-User": "yes",
    "X-Guest-Token": guest_token,
}

session = requests.Session()

task1 = session.post('https://api.twitter.com/1.1/onboarding/task.json',
	params={
		'flow_name': 'login',
		'api_version': '1',
		'known_device_token': '',
		'sim_country_code': 'us'
	},
	json={
		"flow_token": None,
		"input_flow_data": {
			"country_code": None,
			"flow_context": {
				"referrer_context": {
					"referral_details": "utm_source=google-play&utm_medium=organic",
					"referrer_url": ""
				},
				"start_location": {
					"location": "deeplink"
				}
			},
			"requested_variant": None,
			"target_user_id": 0
		}
	},
	headers=twitter_header
)

session.headers['att'] = task1.headers.get('att')
task2 = session.post('https://api.twitter.com/1.1/onboarding/task.json', 
	json={
        "flow_token": task1.json().get('flow_token'),
        "subtask_inputs": [{
                "enter_text": {
                    "suggestion_id": None,
                    "text": username,
                    "link": "next_link"
                },
                "subtask_id": "LoginEnterUserIdentifier"
            }
        ]
    },
	headers=twitter_header
)

task3 = session.post('https://api.twitter.com/1.1/onboarding/task.json', 
	json={
        "flow_token": task2.json().get('flow_token'),
        "subtask_inputs": [{
                "enter_password": {
                    "password": password,
                    "link": "next_link"
                },
                "subtask_id": "LoginEnterPassword"
            }
        ],
    },
	headers=twitter_header
)

task4 = session.post('https://api.twitter.com/1.1/onboarding/task.json', 
	json={
        "flow_token": task3.json().get('flow_token'),
        "subtask_inputs": [{
                "check_logged_in_account": {
                    "link": "AccountDuplicationCheck_false"
                },
                "subtask_id": "AccountDuplicationCheck"
            }
        ]
    },
	headers=twitter_header
).json()

for t4_subtask in task4.get('subtasks', []):
	if 'open_account' in t4_subtask:
		authentication = t4_subtask['open_account']
		break
	elif 'enter_text' in t4_subtask:
		response_text = t4_subtask['enter_text']['hint_text']
		code = input(f'Requesting {response_text}: ')
		task5 = session.post('https://api.twitter.com/1.1/onboarding/task.json', json={
			"flow_token": task4.get('flow_token'),
			"subtask_inputs": [{
				"enter_text": {
					"suggestion_id": None,
					"text": code,
					"link": "next_link"
				},
				"subtask_id": "LoginAcid"
			}]
		}, headers=twitter_header).json()
		print("task5:")
		print(task5)
		for t5_subtask in task5.get('subtasks', []):
			print("t5_subtask:")
			print(t5_subtask)
			if 'open_account' in t5_subtask:
				authentication = t5_subtask['open_account']

if not authentication:
	print("Failed to authenticate")
	exit(1)

print()
print("In terminal, run the following command:")
print(f"echo '{json.dumps([authentication])}' > nitter-guest_accounts.json")
