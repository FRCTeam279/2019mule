import math
import wpilib
from wpilib.command.subsystem import Subsystem
from wpilib import SmartDashboard

import subsystems
import robotmap

class HatchGrab(Subsystem):
    def __init__(self):
        print('HatchGrab: init called')
        super().__init__('HatchGrab')
        self.logPrefix = "HatchGrab: "
    
    self.servo1 = wpilib.PWM(robotmap.cargograb)

    self.servo2 = wpilib.PWM(robotmap.cargograb