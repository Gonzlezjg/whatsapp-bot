from twilio.rest import Client
from dotenv import load_dotenv
import os
import openai

load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')

account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
whatsapp_number = os.getenv('TWILIO_WHATSAPP_NUMBER')

client = Client(account_sid, auth_token)


wsNumber = 'whatsapp:'

def translate(text):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"{text}",
        n=1,
        temperature=0.5,
        max_tokens=2048,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response['choices'][0]['text']

def send_message(to, body):
    message = client.messages.create(
  from_=wsNumber,
  body=body,
  to={to}
)
    return message.sid

def respond_to_message(message_sid):
    message = client.messages.get(message_sid).fetch()
    text = message.body
    fromText = message.from_
    translated_text = translate(text)
    send_message(message.from_, translated_text)

