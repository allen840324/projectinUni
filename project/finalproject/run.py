import RPi.GPIO as GPIO
import time
import myemail
import PTQS1005
import thingspeak
import db_calculater
import serial
from serial import SerialException
import smtplib
import sys
import urllib.request
from urllib.request import urlopen
import _thread
import pyaudio
import os
from math import log10
from statistics import mean

GPIO.setmode(GPIO.BOARD)

GPIO.setup(11, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)

def main():
    
    while True:
        t1=time.time()
        #count=0
        PTQS=PTQS1005.ptq()
        PM25=int(PTQS[0])
        #print(PM25)
        #print(type(PM25))
        CO2=int(PTQS[3])
        Tem=float(PTQS[4])
        thingspeak.get(t1)
        db_meter = db_calculater.listen(t1)
        print(db_meter)
        dB=0
        time.sleep(10)
        #if count==5:
            #print("取出5次")   
            #break
        #count=count+1
        
        if Tem>50 and CO2>1500 and PM25>100:
            sendemail()
            GPIO.output(11,False)
            GPIO.output(12,False)
            GPIO.output(13,False)
            GPIO.output(15,False)
            time.sleep(20)
            continue
        elif CO2>800:
            GPIO.output(15,True)
        if Tem>30 and dB>50 :
         GPIO.output(11,True)#strong
         GPIO.output(12,True)
         GPIO.output(13,True)
         time.sleep(2)
         GPIO.output(11,False)
         GPIO.output(12,False)
         GPIO.output(13,False)
         time.sleep(2)
         continue
        elif 30>Tem>20 or 50>dB>40:
         GPIO.output(11,True)#mid
         GPIO.output(12,True)
         time.sleep(2)
         GPIO.output(11,False)
         GPIO.output(12,False)
         time.sleep(2)
         continue
        elif Tem<20 or 40>dB>30:
         GPIO.output(11,True)#weak
         time.sleep(2)
         GPIO.output(11,False)
         time.sleep(2)
         continue
        elif CO2<800:
            if Tem>30 and dB>60:
                GPIO.output(11,True)#strong
                GPIO.output(12,True)
                GPIO.output(13,True)
                time.sleep(2)
                GPIO.output(11,False)
                GPIO.output(12,False)
                GPIO.output(13,False)
                time.sleep(2)
                continue
        elif 30>Tem>20 or 50>dB>40:
         GPIO.output(11,True)#mid
         GPIO.output(12,True)
         time.sleep(2)
         GPIO.output(11,False)
         GPIO.output(12,False)
         time.sleep(2)
         continue
        elif Tem<20 and 40>dB>30 :
         GPIO.output(11,True)#weak 
         time.sleep(2)
         GPIO.output(11,False) 
         time.sleep(2)
         continue
    GPIO.cleanup()    
    return 0

if __name__ == '__main__':
    main()

