"""This module can be used to send emails."""

import yagmail

def email(semail, passwd, remail, sub, message):
    """This function takes 5 arguments, i.e.,
    semail - Sender's Email,
    passwd - App password (Refer Google to generate App password),
    remail - Receiver's Email,
    sub - Subject of mail,
    message - Body of mail
    """
    receiver = remail
    body = message
    subject = sub

    yag = yagmail.SMTP(semail, passwd)
    yag.send(to=receiver, subject=subject, contents=body)

    print("Email sent successfully!")