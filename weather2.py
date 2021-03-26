#!/usr/bin/env python3

import sys
import RPi.GPIO as GPIO
import os
import time
from time import sleep
import Freenove_DHT as DHT
import urllib3

DHTPin = 11     #define the pin of DHT11

def loop():
    dht = DHT.DHT(DHTPin)   #create a DHT class object
    counts = 0 # Measurement counts
    while(True):
        counts += 1
        print("Measurement counts: ", counts)
        for i in range(0,15):            
            chk = dht.readDHT11()     #read DHT11 and get a return value. Then determine whether data read is normal according to the return value.
            if (chk is dht.DHTLIB_OK):      #read DHT11 and get a return value. Then determine whether data read is normal according to the return value.
                print("DHT11,OK!")
                break
            time.sleep(0.1)
        print("Humidity : %.2f, \t Temperature in C: %.2f \n"%(dht.humidity,dht.temperature))
        if dht.humidity > 70:
          print("Humid Environment. Damage Risk.")
        elif dht.temperature > 37:
          print("High Temperature. Damage Risk.")  
        elif dht.humidity > 70 and dht.temperature > 37:
          print("Hot and Humid. Damage Risk.")
        elif dht.temperature < 15:
          print("Low Temperature. Damage Risk.")
        elif dht.humidity < 40:
          print("Dry Environment. Damage Risk.")
        elif dht.humidity < 40 and dht.temperature < 15:
          print("Cold and Dry. Damage Risk.")
        else:
          print("Working Conditions")
          break
        time.sleep(2)       
        
if __name__ == '__main__':
    print ('Program is starting ... ')
    try:
        loop()
    except KeyboardInterrupt:
        GPIO.cleanup()
        exit()  


