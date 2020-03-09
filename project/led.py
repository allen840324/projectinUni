import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(11, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)

for x in range (0,3):
 GPIO.output(11,True)
 time.sleep(1)
 GPIO.output(11,False)
 time.sleep(1)
 GPIO.output(12,True)
 time.sleep(1)
 GPIO.output(12,False)
 time.sleep(1)
 GPIO.output(13,True)
 time.sleep(1)
 GPIO.output(13,False)
 time.sleep(1)
 GPIO.output(15,True)
 time.sleep(1)
 GPIO.output(15,False)
 time.sleep(1)
GPIO.cleanup()
