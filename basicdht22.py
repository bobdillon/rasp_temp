import Adafruit_DHT
import RPi.GPIO as GPIO

#make class instane by passing sensor type
DHT_SENSOR = Adafruit_DHT.DHT22

#set gpio for data pin
DHT_PIN = 4

#set which numbering schema the gpio library will use - BCM or board
#broadcom SOC channel number -> BCM
GPIO.setmode(GPIO.BCM)

#use internal resistor to start dat pin on high
GPIO.setup(DHT_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)


while True:
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
    
    if humidity is not None and temperature is not None:
        temp_f = temperature * 9/5 +32
        print("Temp C = {0:0.1f}*C Temp F = {1:0.1f}=*F Humidity = {2:0.1f}%".format(temperature,temp_f,humidity))
    else:
        print("Failed to retrieve from the sensor.")