"""This module can be used to send SMS via mobile using Twilio. Register at Twilio to get Account sid, Auth token and Twilio phone number."""

from twilio.rest import Client

def mobilesms(sid, token, text, tnum, rnum):
    """This function takes 5 arguments as String, i.e.,
    sid - Twilio Account sid,
    token - Twilio Auth token,
    text - Text to be sent,
    tnum - Twilio number,
    rnum - Recipient's number (must be verified in Twilio).
    """
    account_sid = sid
    auth_token = token
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body= text,
        from_= tnum,
        to= rnum
    )

    print(message.sid)