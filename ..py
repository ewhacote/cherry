import json
import requests
from bs4 import BeautifulSoup
import datetime
from nacl.signing import VerifyKey
from nacl.exceptions import BadSignatureError
import pytz
import json
import boto3

client = boto3.client('sns')
PUBLIC_KEY = '505cf99b969a8b45944436799020020c93fd80f16948ba86ea36c1031f3b9f24'
PING_PONG = {"type": 1}
RESPONSE_TYPES = {"PONG": 1,
                  "ACK_NO_SOURCE": 2,
                  "MESSAGE_NO_SOURCE": 3,
                  "MESSAGE_WITH_SOURCE": 4,
                  "ACK_WITH_SOURCE": 5}


def verify_signature(event):
    raw_body = event.get("rawBody")
    signature = event['params']['header'].get('x-signature-ed25519')
    timestamp = event['params']['header'].get('x-signature-timestamp')

    verify_key = VerifyKey(bytes.fromhex(PUBLIC_KEY))
    verify_key.verify(f'{timestamp}{raw_body}'.encode(), bytes.fromhex(signature))


def ping_pong(body):
    if body.get("type") == 1:
        return True
    return False


def lambda_handler(event, context):
    # verify the signature
    try:
        verify_signature(event)
    except Exception as e:
        raise Exception(f"[UNAUTHORIZED] Invalid request signature: {e}")
    # check if message is a ping
    body = event.get('body-json')
    if ping_pong(body):
        return PING_PONG

    if body.get("type") == 2:
        return command_handler(body)

    # dummy return
    return {
        "type": RESPONSE_TYPES['MESSAGE_NO_SOURCE'],
        "data": {
            "tts": False,
            "content": "BEEP BOOP",
            "embeds": [],
            "allowed_mentions": []
        }
    }


def command_handler(b):
    command = b['data']['name']
    if command == 'rice':
        url = "http://ewha.ac.kr/ewha/life/restaurant.do?mode=view&articleNo=905&article.offset=0&article"
        response = requests.get(url)
        soup = BeautifulSoup(response.text)
        obj = soup.find_all(attrs={'class': 'b-menu-day mon'})
        for ob in obj:
            dt = datetime.datetime.today().strftime("(%m.%d)")
            data = ob.find_all("div")
            if dt == data[0].text.split()[1]:
                try:
                    content = data[0].text.split()[0] + data[0].text.split()[1] + data[2].text
                except:
                    content = "no menu today"
                break
        return {
            'type': 4,
            'data': {'content': content}
        }


    elif command == 'time':
        timeZ_S = pytz.timezone('Asia/Seoul')
        dt = datetime.datetime.now(timeZ_S)
        return {'type': 4,
                'data': {'content': dt.strftime('%Y-%m-%d %H:%M:%S %Z %z')}
                }
    elif command == 'email':
        snsArn = 'arn:aws:sns:ap-northeast-2:232871681232:HW3'
        message = "My name is Chaeri Kim (2071018)"

        response = client.publish(
            TopicArn=snsArn,
            Message=message,
        )
        return {'type': 4,
                'data': {'content': message}
                }