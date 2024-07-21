import pyemail
import pysearch
import pylocate
import pytalk
import pyvolume
import pysms
import pymsms
import pybemail

print("""Welcome to Python Menu Program!\n
Select which task you want to perform from the below Menu.\n""")
print("""\t\t-----MENU-----\n
\t\t    Email\n
\t\t     SMS\n
\t\t Google Search\n
\t\t Geo-Location\n
\t\t Text-to-Audio\n
\t\t Volume Control\n
\t\t SMS via Mobile\n
\t\t   Bulk Email\n
\t\t      Exit\n""")

while True:
    choice = input("Tell me and I will do it! ")
    
    if ("email" in choice):
    
        print("You have chosen to send Email")
        sender_email = input("Enter Sender's Email: ")
        app_password = input("Enter App Password: ")
        receiver_email = input("Enter Receiver's Email: ")
        subject = input("Enter Mail Subject: ")
        body = input("Enter message body: ")
    
        pyemail.email(sender_email, app_password, receiver_email, subject, body)
        
    
    elif ("sms" in choice):
    
        print("You have chosen to send SMS")
        api_key = input("Enter Textlocal Api Key: ")
        sender_id = input("Enter Textlocal approved Sender id: ")
        number = input("Enter Receiver's mobile number: ")
        message = input("Enter Textlocal approved template message: ")
    
        pysms.sms(api_key, sender_id, number, message)
        
    
    elif ("google" in choice or "search" in choice):
    
        print("You have chosen to Google Search")
        query = input("Enter what you want to search on Google: ")
        results = input("Enter number of results you want: ")
        api_key = input("Enter SerpApi Api Key: ")
    
        pysearch.google_search(query, results, api_key)
        
    
    elif ("geo" in choice or "locate" in choice or "location" in choice):
    
        print("You have chosen to Geo-Locate")
        ip = input("Enter the IP Address: ")
    
        pylocate.geo(ip)
        
    
    elif ("text" in choice or "audio" in choice):
    
        print("You have chosen convert Text-to-Audio")
        text = input("Enter text to be spoken: ")
        volume = float(input("Enter the volume of the voice between 0.1 - 1.0: "))
        voice = int(input("Enter 1 for Female voice and 0 for Male voice: "))
    
        pytalk.textspeech(text, volume, voice)
        
    
    elif ("volume" in choice or "control" in choice):
    
        print("You have chosen to control System Volume")
        volume = int(input("Enter the volume between 1 - 100: "))
    
        pyvolume.set_volume(volume)
    
    elif ("smsmobile" in choice or "mobile" in choice):
    
        print("You have chosen to SMS via Mobile")
        account_sid = input("Enter Twilio Account sid: ")
        auth_token = input("Enter Twilio Auth token: ")
        message = input("Enter Text to be sent: ")
        twilio_number = input("Enter the Twilio number: ")
        receiver_number = input("Enter the Receiver's number verified in Twilio: ")
    
        pymsms.mobilesms(account_sid, auth_token, message, twilio_number, receiver_number)
    
    elif ("bulk" in choice or "bulkemail" in choice):
    
        print("You have chosen to Bulk Email")
        sender_email = input("Enter Sender's Email: ")
        app_password = input("Enter App Password: ")
        subject = input("Enter Mail Subject: ")
        body = input("Enter message body: ")
        file_name = input("Enter name of the file with .csv extension: ")
    
        pybemail.bemail(sender_email, app_password, subject, body, file_name)
    
    elif ("exit" in choice):
        break
    
    else:
        print("Please check your choice, it should relate to the MENU. Try again !")