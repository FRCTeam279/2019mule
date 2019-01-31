import math

from wpilib.BaseSolenoid import DoubleSolenoid
from wpilib.command import Command
import robotmap
import subsystems
import oi

class TankDriveLift():

    def __init__(self):
            super().__init__('TankDriveLift')
            self.setInterruptible(True)
            self.setRunWhenDisabled(False)

    def execute(self):


    def isFinished(self):
        # default commands never "finish", they're just interrupted by other commands
        return False
