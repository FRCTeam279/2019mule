import math
import wpilib
from wpilib.command.subsystem import Subsystem
from wpilib import SmartDashboard
from wpilib.driverstation import DriverStation
from wpilib.doublesolenoid import DoubleSolenoid

import subsystems
import robotmap

class TankLift(Subsystem):

    def __init__(self):
        print('TankLift: init called')
        super().__init__('TankLift')
        self.logPrefix = "TankLift: "

        self.frontCylinder = wpilib.DoubleSolenoid(1,2) # takes ports on pcm to energize solenoid
        self.rearCylinder =  wpilib.DoubleSolenoid(3,4)
    # ------------------------------------------------------------------------------------------------------------------

 
    def driveLift(self):       # reads the lift trigger from the right joystick
        '''
        if liftTrig:
            on_off = 1.0
        else:
            on_off = 0.0
            '''
        self.frontCylinder.set(1)   # 1: extend, 2: retract, 0: off
        self.rearCylinder.set(1)
   
