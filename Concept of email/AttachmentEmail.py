# Example of Sending Email With Attachment
#
# @author SunilOS
# @version 1.0
# @Copyright (c) SunilOS
# @Url www.SunilOs.com
#

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

fromaddr = "anshikashrivansh@gmail.com"
toaddr = "anshikashrivansh@gmail.com"

# instance of MIMEMultipart
msg = MIMEMultipart()

# storing the senders email address
msg['From'] = fromaddr

# storing the receivers email address
msg['To'] = toaddr

# storing the subject
msg['Subject'] = "This is the Document Attachted"

# string to store the body of the mail
body = "Below is the Attachment"

# attach the body with the msg instance
msg.attach(MIMEText(body, 'plain'))

# open the file to be sent
filename = "Serialization.txt"
attachment = open("D://Anshika//Python//Serialization.txt","rb")

# instance of MIME Base and named as p
p = MIMEBase('application', 'octet-stream')

# To change the payload into encoded form
p.set_payload((attachment).read())

# encode into base64
encoders.encode_base64(p)

p.add_header('Content-Disposition', "attachment; filename= %s" % filename)

# attach the instance 'p' to instance 'msg'
msg.attach(p)

# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)

# start TLS for security
s.starttls()

# Authentication
s.login(fromaddr, "mhjz yatn kmlj yqhk")

# Converts the Multipart msg into a string
text = msg.as_string()

# sending the e-mail
s.sendmail(fromaddr, toaddr, text)

# terminating the session
s.quit()