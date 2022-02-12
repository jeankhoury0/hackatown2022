from twilio.rest import Client

import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())
class SmsController:
    account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
    auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
    client = Client(account_sid, auth_token)

    def __init__(self, to, body):
        self.to = to
        self.body = body

    def sendSMS(self):
        message = self.client.messages \
            .create(
                body = self.body,
                from_ = '+18507610242',
                to=self.to
            )
        return message

