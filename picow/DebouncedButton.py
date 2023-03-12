import utime
from machine import Pin

class DebouncedButton:
    debounceTime = 300
    def __init__(self, pinNum, handler, pull=Pin.PULL_DOWN, trigger=Pin.IRQ_RISING):
        self.lastPressed = 0
        self.button = Pin(pinNum, Pin.IN, pull=pull)
        self.handler = handler
        self.button.irq(handler=self._internalHandler, trigger=trigger)
    
    def _internalHandler(self, pin):
        curTime = utime.ticks_ms()
        if curTime > self.lastPressed + DebouncedButton.debounceTime:
            self.lastPressed = curTime
            self.handler(pin)
