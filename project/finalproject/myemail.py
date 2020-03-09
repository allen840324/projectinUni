
import smtplib
import time
def sendemail():
	smtpUser = 'allen840324@gmail.com'
	smtpPass = 'j960048e7j8id'

	toAdd = 'allen840324@gmail.com'
	fromAdd = smtpUser

	subject ='FireAlarm'
	header = 'To: '+toAdd+'\n'+'From: '+fromAdd+'\n'+'Subject: '+subject
	body = '324'
	print(header)


	s = smtplib.SMTP('smtp.gmail.com',587)

	s.ehlo()
	s.starttls()
	s.ehlo()

	s.login(smtpUser,smtpPass)
	s.sendmail(fromAdd,toAdd,header+'\n'+body)
	print('Fire Alarm is sent')
	s.quit
#sendemail()
