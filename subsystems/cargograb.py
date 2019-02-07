# Two servos to raise and lower the door that keeps the ball from falling out
# Contains the cargo
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
    
    self.servo1 = wpilib.PWM(robotmap.cargograb)

    self.servo2 = wpilib.PWM(robotmap.cargograb)
#-----------------------------------------------------------------------------------------


'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    def initDefaultCommand(self):
        self.setDefaultCommand(CargoGrabControls())
        print("{}Default command set to CargoGrab".format(self.logPrefix)) 
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

    def openCargoHold(self):

        

