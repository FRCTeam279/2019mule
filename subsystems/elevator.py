import math
import wpilib
from wpilib.command.subsystem import Subsystem
from wpilib import SmartDashboard
from commands.elevatormoveup import ElevatorMoveUp
from commands.elevatormovedown import ElevatorMoveDown

import subsystems
import robotmap

"""
The elevator raises and lowers the grabber mechanisms
it uses a forklift style lift with three bars that slide against each other
it is powered with a 775 motor, a speed controller, an encoder to read the height,
and a limit switch at the bottom to stop it from over moving.

The motor pulls a string to lift the system. use the encoder to monitor the distance
(or discuss another potentiometer system like last year)

i need to add speed controller operatios, and encoder code to meaasure the height.
"""

class Elevator(Subsystem):
 
    def __init__(self):
        print('Elevator: init called')
        super().__init__('Elevator')
        self.logPrefix = "Elevator: "

        self.btmLimitSwitch = wpilib.DigitalInput(robotmap.elevator.btmLimitSwitchPort)
        self.elevatorSpdCtrl = wpilib.Talon(robotmap.elevator.elevatorMotorPort) # may need to change this to VictorSP?

        self.elevatorLastSpeedSet = 0.0

# ------------------------------------------------------------------------------------------------------------------
    
    def initDefaultCommand(self):
        self.setDefaultCommand(ElevatorTeleopDefault) #change
        print("{}Default command set to ElevatorControls".format(self.logPrefix))

    def stopElevator(self):
        self.elevatorSpdCtrl.set(0.0)

    def holdElevator(self):
        if self.btmLimitSwitch():
            self.elevatorSpdCtrl.set(0.0)
            self.elevatorLastSpeedSet = 0.0  #this is an example from last years code
        else:
            self.elevatorSpdCtrl.set(robotmap.elevator.elevatorHoldSpeed) #Add elevatorHoldSpeed to robotmap
            self.elevatorLastSpeedSet = robotmap.elevator.elevatorHoldSpeed

    def rawMove(self, speed):
        self.elevatorSpdCtrl.set(speed)

# ---------------------------------------------
# Elevator Movement
# ---------------------------------------------


    def elevatorMoveUp(self, speed):
    #    need to work on this
        pass

    def elevatorMoveDown(self, speed):
        if not self.btmLimitSwitch():
            self.elevatorSpdCtrl.set(speed)
            self.elevatorLastSpeedSet = speed
            return

        else
            self.elevatorSpdCtrl.set(0.0)
            self.elevatorLastSpeedSet = 0.0

    def elevatorBottomLimit(self):
        if robotmap.elevator.elevatorBtmLimitNormalClosed:
            return not self.btmLimitSwitch.get()
        else:
            return self.btmLimitSwitch.get()