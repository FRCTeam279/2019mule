import math
import wpilib
from wpilib.command.subsystem import Subsystem
from wpilib import SmartDashboard
from commands.elevatorcontrols import ElevatorControls

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
        print('Elevator: init called')
        super().__init__('Elevator')
        self.logPrefix = "Elevator: "

        self.elevatorSpdCtrl = wpilib.Talon(robotmap.elevatorSystem.elevatorMotorPort) # may need to change this to victor?
        """
        if robotmap.driveLine.invertRight: would have to add this into robotmap
            self.elevatorSpdCtrl.setInverted(False)
        """
        self.btmLimitSwitch = wpilib.DigitalInput(robotmap.elevatorSystem.btmLimitSwitchPort)

# ------------------------------------------------------------------------------------------------------------------
    def initDefaultCommand(self):
        self.setDefaultCommand(ElevatorControls())
        print("{}Default command set to ElevatorControls".format(self.logPrefix))

        #set the default to be contolled with the joystyicks and have the other commands interupt it

    def elevatorMove(self):
        self.elevatorSpdCtrl.set(0.0) #need to make the variables for this

    #def stop(self):
    #    self.elevatorSpdCtrl.set(0.0)