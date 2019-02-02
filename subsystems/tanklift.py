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

        self.frontCylinder = wpilib.DoubleSolenoid(1,0,1) # 1st arg= CAN ID=1, then takes ports on pcm to energize solenoid
        self.rearCylinder =  wpilib.DoubleSolenoid(1,2,3) # 1st arg= CAN ID=1, ...
    # ------------------------------------------------------------------------------------------------------------------

 
    def extendAll(self):       # reads the lift trigger from the right joystick
        self.frontCylinder.set(1)   # 1: extend, 2: retract, 0: off
        self.rearCylinder.set(1)
   
    def retractAll(self):       # reads the lift trigger from the right joystick
        self.frontCylinder.set(2)   # 1: extend, 2: retract, 0: off
        self.rearCylinder.set(2)

    def extendFront(self):       # reads the lift trigger from the right joystick
        self.frontCylinder.set(1)   # 1: extend, 2: retract, 0: off
        self.rearCylinder.set(2)

    def extendBack(self):       # reads the lift trigger from the right joystick
        self.frontCylinder.set(2)   # 1: extend, 2: retract, 0: off
        self.rearCylinder.set(1)
        #this may not be needed in the actual sequence of final robot since the front will always be extended when the back extends
   
    # more functions for sophisticated functionality