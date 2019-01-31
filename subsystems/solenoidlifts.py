"""
pcm object, should read the pressure too for the valve and trigger the compressor
compressor object, to read and control pressure, you may not need this. should be hardwired with ther pcm
sol front
sol back

put in logic for enablin the solenoids in this subsytem so you dont have to repeat it

you DONT have to set up anything for CAN
"""
import math
import wpilib
from wpilib.command.subsystem import Subsystem

import subsystems
import robotmap

class Solenoids(Subsystem):

    def __init__(self):
        print('Solenoids: init called')
        super().__init__('Solenoids')
        self.logPrefix = "Solenoids: "   # not sure what this does

    def triggerSolenoids()

        self.pcm
    

        self.frontSol


        self.backSol


    def initDefaultCommand(self):
                self.setDefaultCommand(TankDriveLift())
                print("{}Default command set to TankDriveLift".format(self.logPrefix))


    def stop(self):
        #insert stopped default retracted position of solenoids?
