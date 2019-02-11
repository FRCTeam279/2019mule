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
        
        self.r = wpilib.AnalogInput(robotmap.driveLine.RtSensPort)
        #self.r2 = wpilib.AnalogInput(robotmap.driveLine.RtSens2Port)
        #self.r3 = wpilib.AnalogInput(robotmap.driveLine.RtSens3Port)
        self.l = wpilib.AnalogInput(robotmap.driveLine.LftSensPort)
        #self.l2 = wpilib.AnalogInput(robotmap.driveLine.LftSens2Port)
        #self.l3 = wpilib.AnalogInput(robotmap.driveLine.LftSens3Port)
    # ------------------------------------------------------------------------------------------------------------------
    
    def initDefaultCommand(self):
            self.setDefaultCommand(TankDriveTeleopDefaultSkid()) #skid
            print("{}Default command set to DriveTeleopDefaultSkid".format(self.logPrefix))

    def driveRaw(self, left, right):
        forward = left > 0 and right > 0
        r = self.r.get()
        l = self.l1.get()
        tilted = "no tilt"

        if abs(l - r) > 0 and abs(l - r) <= .88 and forward:
            tilted = "small"
        elif abs(l - r) > .88 and abs(l - r) <= 1.4 and forward:
            tilted = "medium"
        elif abs(l - r) > 1.4 and abs(l - r) <= 2.1 and forward:
            tilted = "large"
        else:
            tilted = "no tilt"

        if tilted == "no tilt":
            spdLeft = left
            spdRight = right
        if tilted == "small":
            if (r > l):       # small tilt towards right
               spdRight = max(1,right*(1+robotmap.driveLine.spdCompSmall))
               spdLeft = left
            else:
                spdRight = right
                spdLeft = max(1,left*(1+robotmap.driveLine.spdCompSmall))
        if tilted == "medium":   
            if (r > l):       # large tilt towards right
               spdRight = max(1,right*(1+robotmap.driveLine.spdCompMedium))
               spdLeft = left
            else:
                spdRight = right
                spdLeft = max(1,left*(1+robotmap.driveLine.spdCompLarge))
        if tilted == "large":  
            if (r > l):       # very large tilt towards right
               spdRight = max(1,right*(1+robotmap.driveLine.spdCompLarge))
               spdLeft = left
            else:
                spdRight = right
                spdLeft = max(1,left*(1+robotmap.driveLine.spdCompLarge))
        
        self.leftSpdCtrl.set(spdLeft)
        self.rightSpdCtrl.set(spdRight)
    
    def stop(self):
        self.leftSpdCtrl.set(0.0)
        self.rightSpdCtrl.set(0.0)
