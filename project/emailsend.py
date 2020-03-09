import os
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

def emailsend():
server = 'smtp.gmail.com'
port = 587

msg = MIMEMultipart()
msg['Subject'] = '火警發生'
msg['From'] = 'raspberrypi@gmail.com'
msg['To'] = 'j96004875@gmail.com'

text = MIMEText("感測器位於001的北側,溫度與懸浮粒子濃度超標,疑似發生火警")
msg.attach(text)


s = smtplib.SMTP(server, port)
s.ehlo()
s.starttls()
s.ehlo()

s.login('raspberrypi@gmail.com', 'raspberrypi')
s.sendmail('raspberrypi@gmail.com', 'j96004875@gmail.com', msg.as_string())
s.quit()

if __name__ == '__main__':
   emailsend();