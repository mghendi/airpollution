#!/usr/bin/env python3

import RPi.GPIO as GPIO
import time
import Freenove_DHT as DHT

from PCF8574 import PCF8574_GPIO
from Adafruit_LCD1602 import Adafruit_CharLCD

from time import sleep, strftime
from datetime import datetime

import captureimage

from naive_bayes import names

DHTPin = 11     #define the pin of DHT11

def rules(temp, hum, vis):
    if temp < 30 and hum >= 50 and vis == 'notclear':
        lcd.message('Cloudy - Fog')
    elif temp >= 30 and hum < 50 and vis == 'clear':
        lcd.message('Hot and Dry')
    elif temp >= 30 and hum >= 50 and vis == 'clear':
        lcd.message('Hot and Humid')
    elif temp < 30 and hum < 50 and vis == 'clear':
        lcd.message('Cold and Dry')
    elif temp >= 30 and hum >= 50 and vis == 'notclear':
        lcd.message('Humid - Fog')
    elif temp < 30 and hum < 50 and vis == 'notclear':
        lcd.message('Smog - Air Pol.')
    elif temp >= 30 and hum < 50 and vis == 'notclear':
        lcd.message('Smog - Air Pol.')
    elif temp < 30 and hum >= 50 and vis == 'clear':
        lcd.message('Cold and Windy')
    else:
        lcd.message("Data Error")

def getvisibility(i):
    visibility = names[i]  #import results from Naive Bayes classifier
    return visibility

def loop():
    dht = DHT.DHT(DHTPin)   #create a DHT class object
    mcp.output(3,1)     # turn on LCD backlight
    lcd.begin(16,2)     # set number of LCD lines and columns
    counts = 0 # Measurement counts
    while(True):
        counts += 1
        vis = getvisibility(-1)
        print("Measurement counts: ", counts)
        for i in range(0,15):            
            chk = dht.readDHT11()     #Read DHT11
            if (chk is dht.DHTLIB_OK):    #Determine whether data read from DHT11 is normal according to the return value.  
                print("DHT11,OK!")
                break
            time.sleep(0.1)
        print("Humidity : %.2f, \t Temperature : %.2f \n"%(dht.humidity,dht.temperature))
        print("Visibility : " + vis)
        hum = '{:.0f}'.format( float(dht.humidity))
        temp = '{:.0f}'.format( float(dht.temperature))
        #lcd.clear()
        lcd.setCursor(0,0)  # set cursor position
        lcd.message('Vis : ' + vis + '\n') # display the visibility
        lcd.message('Hum:' + hum + ' Temp:' + temp )# display the humidity
        time.sleep(3)
        lcd.clear()
        rules(int(temp), int(hum), vis)
        time.sleep(3)
    
def destroy():
    lcd.clear()
    
PCF8574_address = 0x27  # I2C address of the PCF8574 chip.
PCF8574A_address = 0x3F  # I2C address of the PCF8574A chip.
# Create PCF8574 GPIO adapter.
try:
    mcp = PCF8574_GPIO(PCF8574_address)
except:
    try:
        mcp = PCF8574_GPIO(PCF8574A_address)
    except:
        print ('I2C Address Error !')
        exit(1)
# Create LCD, passing in MCP GPIO adapter.
lcd = Adafruit_CharLCD(pin_rs=0, pin_e=2, pins_db=[4,5,6,7], GPIO=mcp)
      
if __name__ == '__main__':
    print ('Program is starting ... ')
    try:
        loop()
    except KeyboardInterrupt:
        GPIO.cleanup()
        destroy()
        exit()  


