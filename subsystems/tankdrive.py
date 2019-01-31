import math
import wpilib
from wpilib.command.subsystem import Subsystem
from wpilib import SmartDashboard
from wpilib.driverstation import DriverStation
import wpilib.drive

import subsystems
import robotmap
from commands.tankdriveteleopdefaultskid import TankDriveTeleopDefaultSkid as TankDriveTeleopDefaultSkid

class TankDrive(Subsystem):

    def __init__(self):
        print('TankDrive: init called')
        super().__init__('TankDrive')
        self.logPrefix = "TankDrive: "


        self.leftSpdCtrl = wpilib.Talon(robotmap.driveLine.leftMotorPort)
        if robotmap.driveLine.invertLeft:
            self.leftSpdCtrl.setInverted(True)

        self.rightSpdCtrl = wpilib.Talon(robotmap.driveLine.rightMotorPort)
        if robotmap.driveLine.invertRight:
            self.rightSpdCtrl.setInverted(True)
    # ------------------------------------------------------------------------------------------------------------------
    def initDefaultCommand(self):
            self.setDefaultCommand(TankDriveTeleopDefaultSkid())
            print("{}Default command set to DriveTeleopDefaultSkid".format(self.logPrefix))

    def driveRaw(self, left, right):
        self.leftSpdCtrl.set(left)
        self.rightSpdCtrl.set(right)
    
    def stop(self):
        self.leftSpdCtrl.set(0.0)
        self.rightSpdCtrl.set(0.0)
