from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()

def make_call(to_number: str, message: str = "Stormy is calling you!"):
    account_sid = os.getenv("TWILIO_ACCOUNT_SID")
    auth_token = os.getenv("TWILIO_AUTH_TOKEN")
    from_number = os.getenv("TWILIO_PHONE_NUMBER")

    if not all([account_sid, auth_token, from_number]):
        return "Twilio not set up. Add keys to .env, dummy."

    client = Client(account_sid, auth_token)
    try:
        call = client.calls.create(
            twiml=f'<Response><Say voice="alice">{message}</Say></Response>',
            to=to_number,
            from_=from_number
        )
        return f"Call started! SID: {call.sid}"
    except Exception as e:
        return f"Call failed: {str(e)}"
