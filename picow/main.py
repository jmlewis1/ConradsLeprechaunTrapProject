from machine import Pin, Timer, PWM
from time import sleep
from DebouncedButton import DebouncedButton
from ServoController import ServoController

print("Hello world3!")
#import RPi.GPIO as GPIO

btnPin = 15
pressCount = 0

pin = Pin("LED", Pin.OUT)
indicatorLED = Pin(16, Pin.OUT)
solenoidEnable = Pin(13, Pin.OUT)

servo = ServoController(0, 90)

def handleTestButtonPressed(p):
    print("Handling Test Button")
    servo.setPosition(0)
    solenoidEnable.off()
    indicatorLED.on()

testButton = DebouncedButton(14, handleTestButtonPressed)
irSensor = DebouncedButton(17, handleTestButtonPressed, pull=Pin.PULL_UP, trigger=Pin.IRQ_FALLING)

def handleResetButtonPressed(p):
    global pressCount
    pressCount += 1
    solenoidEnable.on()
    servo.setPosition(90)
    indicatorLED.off()
    print("(%d) Resetting Rising"%(pressCount))

resetButton = DebouncedButton(15, handleResetButtonPressed)

handleResetButtonPressed(None)

while True:
    pin.toggle()
    sleep(1)