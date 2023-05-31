'''**********************************************************************'''
'''
* AYTHOR  : Abdelrahman Osam Khaled
* Date    : 10 May , 2023
* Version : V1.0	
'''
'''**********************************************************************'''

import requests
import json

def send_slack_message(payload, webhook):

    return requests.post(webhook, json.dumps(payload))

webhook = "link here"
payload = {"text": "your name"}
send_slack_message(payload, webhook)