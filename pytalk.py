"""This module can be used to convert text into speech."""

import pyttsx3

def textspeech(text, vol, vocal):
    """This function takes 3 arguments, i.e.,
    text - Write your text to be spoken,
    vol - Set the volume (0.1 for minimum and 1.0 for maximum volume),
    vocal - Set the voice to male or female (0 for male and 1 for female).
    """
    engine = pyttsx3.init()

    volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
    engine.setProperty('volume',vol)

    voices = engine.getProperty('voices')       #getting details of current voice
    engine.setProperty('voice', voices[vocal].id)

    rate = engine.getProperty('rate')   # getting details of current speaking rate
    engine.setProperty('rate', 150)     # setting up new voice rate
    
    engine.say(text)
    engine.runAndWait()