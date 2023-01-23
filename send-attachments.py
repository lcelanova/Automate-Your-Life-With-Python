import os
from email.message import EmailMessage
import ssl
import smtplib
import imghdr


#Define receiver and sender
email_sender = 'lcelanova@gmail.com'
email_receiver = 'lcelanova@gmail.com'

#Creating a password for the program
email_password = 'os.environ.get('EMAIL_PASSWORD')

#Defining subject and body of the email 
subject = 'Look at this'

body = """ This is a project in python that sends you an email with an attachment"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subjetc'] = subject
em.set_content(body)

#attaching the file
with open('pic.jpg','rb') as file:
	file_data = file.read()
	file_type = imghdr.what(file.name)
	file_name = file.name

em.add_attachment(file_data, filename=file_name, subtype=file_type, maintype='image')

mycontext = ssl.create_default_context()

#Defining the server of the sender, port adn context
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=mycontext) as smtp:
	#Log in
	smtp.login(email_sender, email_password)
	#Sending the email
	smtp.sendmail(email_sender, email_receiver, em.as_string())
