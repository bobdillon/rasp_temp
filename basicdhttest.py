#!/usr/bin/python
from matplotlib import pyplot as plt
from matplotlib import style
import Adafruit_DHT
import time
 
 
style.use('ggplot')
 
sensor=11
pin=4
 
y=input('How many seconds do you want in the graphics?')
 
 
tme=[] # cant use time due to sleep function taking it
Temperature=[]
Humidity=[]
for x in range(0,int(y)):
    print('Results: '+str(x))
    humidity,temperature=Adafruit_DHT.read_retry(sensor,pin)
    Temperature.insert(x,temperature)
    Humidity.insert(x,humidity)
    tme.insert(x,x)
    time.sleep(1)
     
 
plt.plot(tme,Humidity,'c',linewidth=5,label='Humidity')    
plt.plot(tme,Temperature,'r',linewidth=5,label='Temperature')
 
plt.title("Room Weather Sensing")
plt.ylabel("TempHumidity (%) and Temp (C)")
plt.xlabel("Sampling Period (s)")
 
plt.legend()
plt.show()