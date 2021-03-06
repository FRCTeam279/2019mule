import math

from wpilib.command import Command
import robotmap
import subsystems
import oi

class CargoTeleopDefault(Command):

    def __init__(self):
            super().__init__('CargoTeleopDefault')
            self.requires(subsystems.elevator)
            self.setInterruptible(True)
            self.setRunWhenDisabled(False)

    def execute(self):
        speed = -(oi.goGamePad.getRawAxis(oi.config.axisCargoGrabIndex))
        subsystems.cargograb.move(speed)

    def isFinished(self):
        # default commands never "finish", they're just interrupted by other commands
        return False

    def interrupted(self):
        subsystems.cargograb.stop()
