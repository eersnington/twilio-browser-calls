from flask import Flask, render_template, jsonify
from flask import request
 
from twilio.jwt.access_token import AccessToken
from twilio.jwt.access_token.grants import VoiceGrant
from twilio.twiml.voice_response import VoiceResponse, Dial
 
from dotenv import load_dotenv, find_dotenv
import os
import pprint as p
from pyngrok import ngrok
from twilio.rest import Client

load_dotenv(find_dotenv(), override=True)

account_sid = os.environ['TWILIO_ACCOUNT']
api_key = os.environ['TWILIO_API_KEY_SID']
api_key_secret = os.environ['TWILIO_API_KEY_SECRET']
twiml_app_sid = os.environ['TWIML_APP_SID']
twilio_auth_token = os.environ['TWILIO_AUTH_TOKEN']
twilio_number = os.environ['TWILIO_NUMBER']
ngrok_token = os.environ['NGROK_AUTH_TOKEN']

print(api_key, api_key_secret, twiml_app_sid, twilio_auth_token, twilio_number, ngrok_token)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template(
        'home.html',
        title="In browser calls",
    )

@app.route('/token', methods=['GET'])
def get_token():
    identity = twilio_number
    outgoing_application_sid = twiml_app_sid

    access_token = AccessToken(account_sid, api_key,
                               api_key_secret, identity=identity)

    voice_grant = VoiceGrant(
        outgoing_application_sid=outgoing_application_sid,
        incoming_allow=True,
    )
    access_token.add_grant(voice_grant)

    response = jsonify(
        {'token': access_token.to_jwt().decode(), 'identity': identity})

    return response

@app.route('/handle_calls', methods=['POST'])
def call():
    p.pprint(request.form)
    response = VoiceResponse()
    dial = Dial(callerId=twilio_number)

    if 'To' in request.form and request.form['To'] != twilio_number:
        print('outbound call')
        dial.number(request.form['To'])
    else:
        print('incoming call')
        caller = request.form['Caller']
        dial = Dial(callerId=caller)
        dial.client(twilio_number)

    return str(response.append(dial))


if __name__ == "__main__":
    port = 8051
    ngrok_tunnel = ngrok.connect(port)
    ngrok_url = ngrok_tunnel.public_url
    print('Public URL:', ngrok_url)
    client = Client(account_sid, twilio_auth_token)

    # Update the Voice URL for your TwiML app
    twiml_app = client.applications(twiml_app_sid).fetch()
    twiml_app.update(voice_url=ngrok_url + "/handle_calls")

    # Run Flask app
    app.run(host='0.0.0.0', port=port, debug=False)