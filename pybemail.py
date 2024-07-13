"""This module can be used to send bulk email using a csv file with all the Email IDs and their respective owners' name."""

import yagmail
import csv

def bemail(semail, passwd, sub, message, file):
    """This function take 5 arguments,i.e.,
    semail - Sender's Email,
    passwd - App password (Refer Google to generate App password),
    sub - Subject of mail,
    message - Body of mail,
    file - Specify name of the file with .csv extension (The file should be present at the location of this module).
    """
    your_email = semail
    app_password = passwd

    yag = yagmail.SMTP(your_email, app_password)

    subject = sub
    salutation= 'Dear {name},\n\n'
    body_template = salutation+message

    recipients_file = file

    with open(recipients_file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
    
        for row in reader:
            receiver_email = row['email']
            receiver_name = row['name']
        
            body = body_template.format(name=receiver_name)
        
            try:
                yag.send(to=receiver_email, subject=subject, contents=body)
                print(f"Email sent successfully to {receiver_email}")
            except Exception as e:
                print(f"Failed to send email to {receiver_email}: {e}")

    print("Bulk email sending completed!")