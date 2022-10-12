#led blink program

import RPi.GPIO as GPIO 
from time import sleep 

GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW) 

while True: 
 GPIO.output(8, GPIO.HIGH) 
 sleep(1) # Sleep for 1 second
 GPIO.output(8, GPIO.LOW) 
 sleep(1) # Sleep for 1 second


#traffic light program


import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BOARD) 
GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW) 
GPIO.setup(10, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(12, GPIO.OUT, initial=GPIO.LOW)
while True: 

#turn red light

 GPIO.output(8, GPIO.HIGH) 
 sleep(2) 
 GPIO.output(8, GPIO.LOW) 
 sleep(2) 

#turn yellow light

 GPIO.output(10, GPIO.HIGH) 
 sleep(2)
 GPIO.output(10, GPIO.LOW) 
 sleep(2) 

#turn green light

 GPIO.output(12, GPIO.HIGH)
 sleep(2) 
 GPIO.output(12, GPIO.LOW) 
 sleep(2)
