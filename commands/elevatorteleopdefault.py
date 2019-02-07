import math

from wpilib.command import Command
import robotmap
import subsystems
import oi

class ElevatorTeleopDefault(Command):

    def __init__(self):
            super().__init__('ElevatorTeleopDefault')
            self.requires(subsystems.elevator)
            self.setInterruptible(True)
            self.setRunWhenDisabled(False)

    def execute(self):
        pass

    def isFinished(self):
        # default commands never "finish", they're just interrupted by other commands
        return False

    def interrupted(self):
        subsystems.elevator.stopElevator()
