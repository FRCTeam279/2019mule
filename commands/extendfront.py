import math

from wpilib.command import Command
import robotmap
import subsystems
import oi

class ExtendFront(Command):

    def __init__(self):
            super().__init__('ExtendFront')
<<<<<<< HEAD
            self.requires(subsystems.drivelift)
=======
>>>>>>> 8e9b3ec75a43d79df9d76be99f51627ba447f1fb
            self.setInterruptible(True)
            self.setRunWhenDisabled(False)

    def execute(self):
        subsystems.drivelift.extendFront()

    def isFinished(self):
        # default commands never "finish", they're just interrupted by other commands
        return True
