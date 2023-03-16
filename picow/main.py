from machine import Pin, Timer, PWM
from time import sleep
import _thread
from DebouncedButton import DebouncedButton
from ServoController import ServoController
from ServoController2 import ServoController2
print("Hello world3!")
#import RPi.GPIO as GPIO

trapTriggered = False

btnPin = 15
pressCount = 0
concurrencyLock = _thread.allocate_lock()

powerLED = Pin("LED", Pin.OUT)

indicatorLED = Pin(16, Pin.OUT)
solenoidDisable = Pin(13, Pin.OUT)

doorServo = ServoController(0, 90)
lockServo = ServoController2(28, 0)
def handleTestButtonPressed(p):
    global trapTriggered
    if concurrencyLock.acquire(False):
        if trapTriggered == False:
            trapTriggered = True
            print("Handling Test Button")
            doorServo.setPosition(0)
            sleep(.5)
            solenoidDisable.off()
            lockServo.setPosition(90)
            sleep(.3)
            solenoidDisable.on()
            indicatorLED.on()
            print("(%d) Set trap Rising"%(pressCount))
        concurrencyLock.release()


testButton = DebouncedButton(14, handleTestButtonPressed)
irSensor = DebouncedButton(17, handleTestButtonPressed, pull=Pin.PULL_UP, trigger=Pin.IRQ_FALLING)

def handleResetButtonPressed(p):
    global pressCount
    global trapTriggered
    if concurrencyLock.acquire(False):
        pressCount += 1
        solenoidDisable.on()
        lockServo.setPosition(180)
        sleep(.5)
        doorServo.setPosition(90)
        indicatorLED.off()
        trapTriggered = False
        print("(%d) Resetting Rising"%(pressCount))
        concurrencyLock.release()

resetButton = DebouncedButton(15, handleResetButtonPressed)

handleResetButtonPressed(None)

while True:
    powerLED.toggle()
    sleep(1)