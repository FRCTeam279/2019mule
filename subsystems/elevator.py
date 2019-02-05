import math
import wpilib
from wpilib.command.subsystem import Subsystem
from wpilib import SmartDashboard

import subsystems
import robotmap

"""
The elevator raises and lowers the grabber mechanisms
it uses a forklift style lift with three bars that slide against each other
it is powered with a 775 motor, a speed controller, an encoder to read the height,
and a limit switch at the bottom to stop it from over moving.

The motor pulls a string to lift the system. use the encoder to monitor the distance
(or discuss another potentiometer system like last year)
"""

class Elevator(Subsystem):
 
    def __init__(self):
        print('TankLift: init called')
        super().__init__('TankLift')
        self.logPrefix = "TankLift: "

        self.elevatorSpdCtrl = wpilib.Talon(robotmap.driveLine.rightMotorPort) # may need to change this to victor?
        """
        if robotmap.driveLine.invertRight:
            self.elevatorSpdCtrl.setInverted(False)
        """
        # variables

# ------------------------------------------------------------------------------------------------------------------
    def initDefaultCommand(self):
        self.setDefaultCommand(TankLiftTeleopDefault())
        print("{}Default command set to TankLiftTeleopDefault".format(self.logPrefix))

    # functions that will be called in command files