from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()

class SmsController:
    
    account_sid = "AC8d3853ec5bde4d8e2be006b412038beb"
    auth_token = '3fb2c2f75640335d724d5a0a527f4825'
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

