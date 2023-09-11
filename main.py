from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from bot import respond_to_message

app = Flask(__name__)

@app.route("/webhook", methods=['POST'])
def webhook():
    message_sid = request.form['MessageSid']
    respond_to_message(message_sid)
    resp = MessagingResponse()
    return str(resp)

if __name__ == "__main__":
    app.run()
