# Two servos acting as a claw, picking up and carrying cargo
# Connected to elevator
import math
import wpilib
from wpilib.command.subsystem import Subsystem
from wpilib import SmartDashboard

import subsystems
import robotmap

class CargoGrab(Subsystem):

    def __init__(self):
        print('CargoGrab: init called')
        super().__init__('CargoGrab')
        self.logPrefix = "CargoGrab: "
    
        self.leftservo = wpilib.PWM(robotmap.cargograb)

        self.rightservo = wpilib.PWM(robotmap.cargograb)
#-----------------------------------------------------------------------------------------


'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    def initDefaultCommand(self):
        self.setDefaultCommand(CargoGrabControls())
        print("{}Default command set to CargoGrab".format(self.logPrefix)) 
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

def openCargoHold(self):
    self.leftservo.set(1.0)
    self.rightservo.set(1.0)

def closeCargoHold(self):
    self.leftservo.set(-1.0)
    self.rightservo.set(-1.0)
        

