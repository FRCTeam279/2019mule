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

'''
Michael's Comments  (delete these lines when done)
Lines 18 and 20 need to be indented so that they are within the __init__(self) function

Instead of naming the servers as server1 and server2, i'd strongly suggest left and right (or top/bottom, front/back, etc..) so that 
it's clear which physical servo is being referred to.  Now having said that, left/right and all the others 
assume you're at the back of the robot looking towards the front.... (same as if it was your person)

THe names of variables in robotmap shoudl be updated to match.  something like 
robotmap.cargograb.rightServoPort 

You'll only need a default command on this subsystem if you want to control the angle of the door with a joystick live, 
as opposed ot just hitting a button to fully open or close.  Maybe that'd be useful.. i don't know.  Try it if you want 
as it'd be good experience to play with even if you don't use it on the production robot.

Definitly plan on having a command to open, and a separate command to close bound to separate buttons
You'll want to store the target angle/setting for each one in the robotmap file
'''


