import os
from email.message import EmailMessage
import ssl
import smtplib


#Define receiver and sender
email_sender = 'lcelanova@gmail.com'
email_receiver = 'lcelanova@gmail.com'

#Creating a password for the program
email_password = 'os.environ.get('EMAIL_PASSWORD')

#Defining subject and body of the email 
subject = 'Look at this'

body = """ This is a proejct in python that sends you an email"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subjetc'] = subject
em.set_content(body)

mycontext = ssl.create_default_context()

#Defining the server of the sender, port adn context
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=mycontext) as smtp:
	#Log in
	smtp.login(email_sender, email_password)
	#Sending the email
	smtp.sendmail(email_sender, email_receiver, em.as_string())
