import math

<<<<<<< HEAD:commands/tankdrivelift.py
from wpilib.BaseSolenoid import DoubleSolenoid
=======
>>>>>>> 69c029165153d86cc5eb6ffd94424e3ab1de0f61:commands/extendall.py
from wpilib.command import Command
import robotmap
import subsystems
import oi

class ExtendAll(Command):

    def __init__(self):
            super().__init__('ExtendAll')
            self.setInterruptible(True)
            self.setRunWhenDisabled(False)

    def execute(self):
        subsystems.drivelift.extendAll()

    def isFinished(self):
        # default commands never "finish", they're just interrupted by other commands
        return True
