import math
import wpilib
from wpilib.command.subsystem import Subsystem
from wpilib.solenoid import Solenoid
from wpilib.digitalinput import DigitalInput

import subsystems
import robotmap

class Ramp(subsystem):
    def __init__(self):
        print("Ramp: init called")
        super().__init__('Ramp')
        self.logPrefix= 'Ramp: '
        self.rampSolenoid = wpilib.solenoid(1,0,1)

    def initDefaultCommand(self):
        self.setDefaultCommand(RampControls())
        print("{}Default command set to RampControls".format(self.logPrefix)) 
