import math

from wpilib.command import Command
import robotmap
import subsystems
import oi

class ElevatorControls(Command):

    def __init__(self):
            super().__init__('ElevatorControls')
            self.requires(subsystems.elevatorsystem)
            self.setInterruptible(True)
            self.setRunWhenDisabled(False)

    def execute(self):
        subsystems.elevatorsystem.elevatorMove()

    def isFinished(self):
        # default commands never "finish", they're just interrupted by other commands
        return True
