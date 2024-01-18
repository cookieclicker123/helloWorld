import smtplib

sender = "seblogsdon@icloud.com"
reciever = "seblogsdon@icloud.com"
password = "cknf-lscd-dhpe-psbl"
subject = "Python email test"
body = "This is a test email sent from Python"

message = f"""From: {sender}
To: {reciever}
Subject: {subject}\n 
{body}
"""

server = smtplib.SMTP("smtp.mail.me.com", 587)
server.starttls()

try:
    server.login(sender, password)
    print("Logged in")
    server.sendmail(sender, reciever, message)
    print("Email has been sent to", reciever)

except smtplib.SMTPAuthenticationError:
    print("Failed to login due to authentication error")

except Exception as e:
    print("An error occurred:", str(e))
    