# Import smtplib for the actual sending function
import smtplib

# Here are the email package modules we'll need
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart


# Create the container (outer) email message.
msg = MIMEMultipart()
msg['Subject'] = 'Our family reunion'
# me == the sender's email address
# family = the list of all recipients' email addresses
msg['From'] = 'testrobtheserver@sina.com'
msg['To'] = '183800313@qq.com'
msg.preamble = 'Our family reunion'


# Send the email via our own SMTP server.
s = smtplib.SMTP('localhost')
s.sendmail('testrobtheserver@sina.com', '183800313@qq.com', msg.as_string())
s.quit()
