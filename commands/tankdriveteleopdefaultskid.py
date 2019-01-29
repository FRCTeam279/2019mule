import math

from wpilib.command import Command
import robotmap 
import subsystems
import oi


class TankDriveTeleopDefaultSkid(Command):
    '''
    One joystick controls rotation, and the other translation
    '''


    def __init__(self):
        super().__init__('TankDriveTeleopDefaultSkid')
        self.requires(subsystems.driveline)
        self.setInterruptible(True)
        self.setRunWhenDisabled(False)


    def execute(self):
<<<<<<< HEAD
        subsystems.driveline.driveRaw(oi.leftDriverStick.getY()*-1.0, oi.rightDriverStick.getY()*-1.0)  # to work correctly: left*1.0, right*-1.0
=======
        subsystems.driveline.driveRaw(oi.leftDriverStick.getY()*-1.0, oi.rightDriverStick.getY()*-1.0)
>>>>>>> ab50d658db9f6f6212742aae4dce6f5a00c194e2

    def isFinished(self):
        # default commands never "finish", they're just interrupted by other commands
        return False
