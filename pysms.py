"""This module can be used to send SMS with the help of Textlocal. Register at Textlocal is necessary to use this module.
Please refer Google on how to get Textlocal Api-key, Sender id and Template message."""

import requests

def sms(key, id, mob, text):
    """This function takes 4 arguments as String, i.e.,
    key - Textlocal Api-key (Create Textlocal account to generate Api-key),
    id - Textlocal approved Sender id,
    mob - Receiver's mobile number (eg- 911234567890),
    text - Textlocal approved template message
    """
    api_key = key
    sender = id
    numbers = mob
    message = text
    url = 'https://api.textlocal.in/send/'

    params = {
        'apikey': api_key,
        'numbers': numbers,
        'message': message,
        'sender': sender
    }

    response = requests.post(url, data=params)
    print(response.json())