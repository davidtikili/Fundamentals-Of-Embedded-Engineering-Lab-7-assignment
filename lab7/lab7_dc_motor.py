import RPi.GPIO as GPIO
import time

MotorPin1 = 11  # pin11
MotorPin2 = 12  # pin12
MotorEnable = 13  # pin13

def setup():
    GPIO.setmode(GPIO.BOARD)  # Numbers GPIOs by physical location
    GPIO.setup(MotorPin1, GPIO.OUT)  # mode --- output
    GPIO.setup(MotorPin2, GPIO.OUT)
    GPIO.setup(MotorEnable, GPIO.OUT)
    GPIO.output(MotorEnable, GPIO.LOW)  # motor stop

def loop():
    while True:
        print('Press Ctrl+C to end the program...')
        GPIO.output(MotorEnable, GPIO.HIGH)  # motor driver enable
        
        # Rotate anticlockwise
        GPIO.output(MotorPin1, GPIO.HIGH)
        GPIO.output(MotorPin2, GPIO.LOW)
        time.sleep(5)
        
        # Stop motor
        GPIO.output(MotorEnable, GPIO.LOW)
        time.sleep(2)
        
        GPIO.output(MotorEnable, GPIO.HIGH)  # motor driver enable
        
        # Rotate clockwise
        GPIO.output(MotorPin1, GPIO.LOW)
        GPIO.output(MotorPin2, GPIO.HIGH)
        time.sleep(5)
        
        # Stop motor
        GPIO.output(MotorEnable, GPIO.LOW)
        time.sleep(2)

def destroy():
    GPIO.output(MotorEnable, GPIO.LOW)  # motor stop
    GPIO.cleanup()  # Release resource

setup()
try:
    loop()
except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be executed.
    destroy()
