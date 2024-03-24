import RPi.GPIO as GPIO
import time

MotorPin1 = 11  # pin11
MotorPin2 = 12  # pin12
MotorEnable = 13  # pin13

YellowLED = 16  # pin15
RedLED = 15  # pin16

def setup():
    GPIO.setmode(GPIO.BOARD)  # Numbers GPIOs by physical location
    GPIO.setup(MotorPin1, GPIO.OUT)  # mode --- output
    GPIO.setup(MotorPin2, GPIO.OUT)
    GPIO.setup(MotorEnable, GPIO.OUT)
    GPIO.setup(YellowLED, GPIO.OUT)
    GPIO.setup(RedLED, GPIO.OUT)
    GPIO.output(MotorEnable, GPIO.LOW)  # motor stop
    GPIO.output(YellowLED, GPIO.LOW)  # yellow LED off
    GPIO.output(RedLED, GPIO.LOW)  # red LED off

def loop():
    while True:
        print('Press Ctrl+C to end the program...')
        GPIO.output(MotorEnable, GPIO.HIGH)  # motor driver enable
        
        # Rotate anticlockwise
        GPIO.output(MotorPin1, GPIO.HIGH)
        GPIO.output(MotorPin2, GPIO.LOW)
        GPIO.output(YellowLED, GPIO.HIGH)  # yellow LED on
        GPIO.output(RedLED, GPIO.LOW)  # red LED off
        time.sleep(5)
        
        # Stop motor
        GPIO.output(MotorEnable, GPIO.LOW)
        GPIO.output(YellowLED, GPIO.LOW)  # yellow LED off
        GPIO.output(RedLED, GPIO.LOW)  # red LED off
        time.sleep(2)
        
        GPIO.output(MotorEnable, GPIO.HIGH)  # motor driver enable
        
        # Rotate clockwise
        GPIO.output(MotorPin1, GPIO.LOW)
        GPIO.output(MotorPin2, GPIO.HIGH)
        GPIO.output(YellowLED, GPIO.LOW)  # yellow LED off
        GPIO.output(RedLED, GPIO.HIGH)  # red LED on
        time.sleep(5)
        
        # Stop motor
        GPIO.output(MotorEnable, GPIO.LOW)
        GPIO.output(YellowLED, GPIO.LOW)  # yellow LED off
        GPIO.output(RedLED, GPIO.LOW)  # red LED off
        time.sleep(2)

def destroy():
    GPIO.output(MotorEnable, GPIO.LOW)  # motor stop
    GPIO.output(YellowLED, GPIO.LOW)  # yellow LED off
    GPIO.output(RedLED, GPIO.LOW)  # red LED off
    GPIO.cleanup()  # Release resource

setup()
try:
    loop()
except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be executed.
    destroy()
