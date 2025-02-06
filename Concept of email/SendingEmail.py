import smtplib
connection = smtplib.SMTP("smtp.gmail.com",587)
connection.ehlo()
connection.starttls()
connection.login("anshikashrivansh@gmail.com","mhjz yatn kmlj yqhk")
connection.sendmail("anshikashrivansh@gmail.com","chinmay27pandit@gmail.com","subject: this is the subject \n\n hello user")
print("Email Sent")
connection.quit()