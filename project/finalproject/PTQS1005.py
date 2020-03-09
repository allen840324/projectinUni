import serial
import time
from serial import SerialException
def ptq():
    try:
        ser = serial.Serial("/dev/ttyUSB0",9600, timeout=10000)
        ser.write(b'\x42\x4D\xAB\x00\x00\x01\x3A')    
        i = 0
        list_sensor=[]
        while True:
            h=ser.read()
            h=int.from_bytes(h, byteorder='little')        
            if i== 4:            
                pm25L=ser.read()
                pm25L=int.from_bytes(pm25L, byteorder='little')
                pm25=str(h*256+pm25L)
                #print(pm25)
                list_sensor.append(pm25)
                i=i+1
                    
            if i==6:          
                TVOCL=ser.read()
                TVOCL=int.from_bytes(TVOCL, byteorder='little')
                TVOC=str(h*256+TVOCL) 
                #print(TVOC)
                list_sensor.append(TVOC)    
                i=i+1

            if i==9:
                HCHOL=ser.read() 
                HCHOL=int.from_bytes(HCHOL, byteorder='little')
                HCHO=str(h*256+HCHOL)
                #print(HCHO)
                list_sensor.append(HCHO)
                i=i+1
                 
            if i==12:
                CO2L=ser.read()
                CO2L=int.from_bytes(CO2L, byteorder='little')
                CO2=str(h*256+CO2L)
                #print(CO2)
                list_sensor.append(CO2)
                i=i+1
                    
            if i==14:
                temL = ser.read()        
                temL=int.from_bytes(temL, byteorder='little')            
                tem=str((h*256+temL)/10.0)
                #print(tem)
                list_sensor.append(tem)
                i=i+1
                    
            if i==16:
                humL = ser.read()
                humL=int.from_bytes(humL, byteorder='little')
                hum=str((h*256+humL)/10.0)
                #print(hum)
                list_sensor.append(hum)
                i=i+1

            i = i + 1        
            if i==24:
                #print(list_sensor[0])
                #print(type(list_sensor[0]))
                #print(list_sensor[1])
                #print(list_sensor[2])
                #print(list_sensor[3])
                #print(list_sensor[4])
                #print(list_sensor[5])
                break
        return list_sensor
    except SerialException:
        list_sensor=[]
        message='感測器未連接'
        list_sensor.append(message)
        list_sensor.append(message)
        list_sensor.append(message)
        list_sensor.append(message)
        list_sensor.append(message)
        list_sensor.append(message)
        #print(list_sensor)
        
        return list_sensor

#ptq()
'''
count = 1
while True:
    ptq()
    
    if(count==5):
        print("取出5次")
        break
    count=count+1
'''
#if __name__ == '__main__':
    #ptq()
