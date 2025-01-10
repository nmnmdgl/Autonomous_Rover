import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
Ena,In1,In2=2,3,4
Enb, In3, In4=17,22,27

GPIO.setup(Ena,GPIO.OUT)
GPIO.setup(In1,GPIO.OUT)
GPIO.setup(In2,GPIO.OUT)
pwm1=GPIO.PWM(Ena,100)
pwm1.start(0)

GPIO.setup(Enb,GPIO.OUT)
GPIO.setup(In3,GPIO.OUT)
GPIO.setup(In4,GPIO.OUT)
pwm2=GPIO.PWM(Enb,100)
pwm2.start(0)

while True:
    GPIO.output(In1,GPIO.LOW)
    GPIO.output(In2,GPIO.HIGH)
    GPIO.output(In3,GPIO.LOW)
    GPIO.output(In4,GPIO.HIGH)
    pwm1.ChangeDutyCycle(100)
    pwm2.ChangeDutyCycle(100)
    sleep(2)
    
    GPIO.output(In1,GPIO.HIGH)
    GPIO.output(In2,GPIO.LOW)
    GPIO.output(In3,GPIO.HIGH)
    GPIO.output(In4,GPIO.LOW)
    pwm1.ChangeDutyCycle(100)
    pwm2.ChangeDutyCycle(100)
    sleep(2)
    
    
"""    GPIO.output(In3,GPIO.LOW)
    GPIO.output(In4,GPIO.HIGH)
    pwm2.ChangeDutyCycle(100)
    sleep(2)
    GPIO.output(In3,GPIO.HIGH)
    GPIO.output(In4,GPIO.LOW)
    pwm2.ChangeDutyCycle(100)
    sleep(2)"""

print("done")
