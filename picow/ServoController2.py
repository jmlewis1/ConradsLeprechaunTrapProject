from machine import Pin, PWM

class ServoController2:
    MAX_POSITION = 7500
    MIN_POSITION = 900
    MAX_ANGLE = 180
    def __init__(self, pinNum, startingAngle):
        self.degrees = 0
        self.position = ServoController2.MIN_POSITION
        self.servo = PWM(Pin(pinNum, Pin.OUT))
        self.servo.freq(50)
        self.setPosition(startingAngle)
        

    def getPosition(self):
        return self.degrees
    
    def setPosition(self, degrees):
        print("Setting servo angle to: %d"%(degrees))
        if degrees > ServoController2.MAX_ANGLE:
            degrees = ServoController2.MAX_ANGLE
        self.degrees = degrees
        pct = float(degrees)/ServoController2.MAX_ANGLE
        print("Servo pct: %f"%(pct))
        self.position = pct * (ServoController2.MAX_POSITION - ServoController2.MIN_POSITION)
        print("Servo offset: %f"%(self.position))
        self.position = int(self.position + ServoController2.MIN_POSITION)
        print("Setting servo position to %d"%(self.position))
        self.servo.duty_u16(self.position)