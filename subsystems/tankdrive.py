import math
import wpilib
from wpilib.command.subsystem import Subsystem
from wpilib import SmartDashboard
from wpilib.driverstation import DriverStation
import wpilib.drive

import subsystems
import robotmap
from commands.tankdriveteleopdefaultskid import TankDriveTeleopDefaultSkid as TankDriveTeleopDefaultSkid
#from commands.tankdriveteleopdefaultnfs import TankDriveTeleopDefaultNFS as TankDriveTeleopDefaultNFS

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
        
        self.r1 = wpilib.AnalogInput(robotmap.driveLine.RtSens1Port)
        self.r2 = wpilib.AnalogInput(robotmap.driveLine.RtSens2Port)
        self.r3 = wpilib.AnalogInput(robotmap.driveLine.RtSens3Port)
        self.l1 = wpilib.AnalogInput(robotmap.driveLine.LftSens1Port)
        self.l2 = wpilib.AnalogInput(robotmap.driveLine.LftSens2Port)
        self.l3 = wpilib.AnalogInput(robotmap.driveLine.LftSens3Port)
    # ------------------------------------------------------------------------------------------------------------------
    
    def initDefaultCommand(self):
            self.setDefaultCommand(TankDriveTeleopDefaultSkid()) #skid
            print("{}Default command set to DriveTeleopDefaultSkid".format(self.logPrefix))

    def driveRaw(self, left, right):
        forward = left > 0 and right > 0
        r1 = self.r1.get()
        r2 = self.r2.get()
        r3 = self.r3.get()
        l1 = self.l1.get()
        l2 = self.l2.get()
        l3 = self.l3.get()
        sensDiff1 = abs(l1-r1)    # 1st left sensor - 1st right sensor
        sensDiff2 = abs(l2-r2)    # 2nd left sensor - 2nd right sensor
        sensDiff3 = abs(l3-r3)    # 3rd left sensor - 3rd right sensor
        tilted = "no tilt"

        if (sensDiff1 >= .2) and forward:
            tilted = "small"
        elif (sensDiff2 >= .2) and forward:
            tilted = "large"
        elif (sensDiff3 >= .2) and forward:
            tilted = "xlarge"
        else:
            tilted = "no tilt"

        if tilted == "no tilt":
            spdLeft = left
            spdRight = right
        if tilted == "small":
            if (r1 > l1):       # small tilt towards right
               spdRight = max(1,right*(1+robotmap.driveLine.spdCompSmall))
               spdLeft = left
            else:
                spdRight = right
                spdLeft = max(1,left*(1+robotmap.driveLine.spdCompSmall))
        if tilted == "large":   # large tilt towards right
            if (r2 > l2):
               spdRight = max(1,right*(1+robotmap.driveLine.spdCompLarge))
               spdLeft = left
            else:
                spdRight = right
                spdLeft = max(1,left*(1+robotmap.driveLine.spdCompLarge))
        if tilted == "xlarge":  # very large tilt towards right
            if (r3 > l3):
               spdRight = max(1,right*(1+robotmap.driveLine.spdCompXLarge))
               spdLeft = left
            else:
                spdRight = right
                spdLeft = max(1,left*(1+robotmap.driveLine.spdCompXLarge))
        
        self.leftSpdCtrl.set(spdLeft)
        self.rightSpdCtrl.set(spdRight)
    
    def stop(self):
        self.leftSpdCtrl.set(0.0)
        self.rightSpdCtrl.set(0.0)
