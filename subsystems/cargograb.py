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
    
        self.leftservo = wpilib.Servo(robotmap.cargograb.leftServoPort)
        self.rightservo = wpilib.Servo(robotmap.cargograb.rightServoPort)
#-----------------------------------------------------------------------------------------


'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def initDefaultCommand(self):
    self.setDefaultCommand(CargoGrabControls())
    print("{}Default command set to CargoGrab".format(self.logPrefix)) 
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

def openCargoHold(self,openbit):
    self.leftservo.set(openbit)
    self.rightservo.set(openbit)

def closeCargoHold(self,closebit):
    self.leftservo.set(closebit)
    self.rightservo.set(closebit)
        

