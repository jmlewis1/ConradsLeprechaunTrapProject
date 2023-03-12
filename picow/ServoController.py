from machine import Pin, PWM

class ServoController:
    MAX_POSITION = 2000000
    MID_POSITION = 1500000
    MIN_POSITION = 1000000
    MAX_ANGLE = 90
    def __init__(self, pinNum, startingAngle):
        self.degrees = 0
        self.position = ServoController.MIN_POSITION
        self.servo = PWM(Pin(0, Pin.OUT))
        self.servo.freq(50)
        self.setPosition(startingAngle)

    def getPosition(self):
        return self.degrees
    
    def setPosition(self, degrees):
        print("Setting servo angle to: %d"%(degrees))
        if degrees > ServoController.MAX_ANGLE:
            degrees = ServoController.MAX_ANGLE
        self.degrees = degrees
        pct = float(degrees)/ServoController.MAX_ANGLE
        print("Servo pct: %f"%(pct))
        self.position = pct * (ServoController.MAX_POSITION - ServoController.MIN_POSITION)
        print("Servo offset: %f"%(self.position))
        self.position = int(self.position + ServoController.MIN_POSITION)
        print("Setting servo position to %d"%(self.position))
        self.servo.duty_ns(self.position)