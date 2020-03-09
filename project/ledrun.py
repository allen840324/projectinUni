import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(11, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)

GPIO.output(11,True)
time.sleep(10)
GPIO.output(12,True)
time.sleep(10)
GPIO.output(13,True)
time.sleep(10)
GPIO.output(13,False)
GPIO.output(15,True)

GPIO.cleanup()
