import sys
import urllib.request
from urllib.request import urlopen
from time import sleep
import PTQS1005
import time
def thingspeak():
# Enter Your API key here
	myAPI = '7D65QCDMUVMSQ2WE' 
# URL where we will send the data, Don't change it
	baseURL = 'https://api.thingspeak.com/update?api_key=%s' % myAPI
	#count=1
	#while true:
	PTQS=PTQS1005.ptq()
	#print(PTQS[0]) print(PTQS[3]) print(PTQS[4]) sleep(5)
		# If Reading is valid
		#if isinstance(humi, float) and isinstance(temp, float):
			# Formatting to two decimal places
			#humi = '%.2f' % humi 					   
			#temp = '%.2f' % temp
			
# Sending the data to thingspeak
	print("data sending...")
	conn = urllib.request.urlopen(baseURL + '&field1=%s&field2=%s&field3=%s' % (PTQS[0], PTQS[3], PTQS[4]))
#print conn.read()
			# Closing the connection
	conn.close()
	print("finish")
		#else:
			#print 'Error'
		# DHT22 requires 2 seconds to give a reading, so make sure to add delay of above 2 seconds.
	sleep(2)
def get(t1):
	while True:
		t2=time.time()
		thingspeak()
		if(t2-t1>11):
			break
