import math

from wpilib.BaseSolenoid import BaseSolenoid #Or from wpilib.BaseSolenoid import DoubleSolenoid???
from wpilib.command import Command
import robotmap
import subsystems
import oi

class Liftfront(): #need to change this

    def __init__(self):
            super().__init__('can.BusABC')
            self.setInterruptible(True)
            self.setRunWhenDisabled(False)

    def execute(self):
        #insert can stuff 


    def isFinished(self):
        # default commands never "finish", they're just interrupted by other commands
        return False
