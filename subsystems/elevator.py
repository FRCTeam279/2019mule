import math
import wpilib
from wpilib.command.subsystem import Subsystem
from wpilib import SmartDashboard
from commands.elevatormoveup import ElevatorMoveUp
from commands.elevatormovedown import ElevatorMoveDown
from commands.elevatorteleopdefault import ElevatorTeleopDefault

import subsystems
import robotmap

"""
The elevator raises and lowers the grabber mechanisms
it uses a forklift style lift with three bars that slide against each other
It is powered with a 775 motor, a speed controller, an encoder to read the height,
and a limit switch at the bottom to stop it from over moving.

The motor pulls a string to lift the system. use the encoder to monitor the distance
(or discuss another potentiometer system like last year)

I need to add speed controller operatios, and encoder code to measure the height.
"""

class Elevator(Subsystem):
 
    def __init__(self):
        print('Elevator: init called')
        super().__init__('Elevator')
        self.logPrefix = "Elevator: "

        self.btmLimitSwitch = wpilib.DigitalInput(robotmap.elevator.btmLimitSwitchPort)
        self.elevatorSpdCtrl = wpilib.VictorSP(robotmap.elevator.elevatorMotorPort) # or could be talon
        
        #reconfigure these ports in robotmap later
        self.elevatorEncoder = wpilib.Encoder(robotmap.elevator.elevatorEncAPort, robotmap.elevator.elevatorEncBPort, robotmap.elevator.elevatorEncReverse, robotmap.elevator.elevatorEncType)
        self.elevatorEncoder.setDistancePerPulse(robotmap.elevator.inchesPerTick)

        #self.elevatorLastSpeedSet = 0.0

# ------------------------------------------------------------------------------------------------------------------
    
    def initDefaultCommand(self):
        self.setDefaultCommand(ElevatorTeleopDefault()) #change
        print("{}Default command set to ElevatorTeleopDefault".format(self.logPrefix))

    def stopElevator(self):
        self.elevatorSpdCtrl.set(0.0)

    def holdElevator(self):
        if self.btmLimitSwitch():
            self.elevatorSpdCtrl.set(0.0)
            #self.elevatorLastSpeedSet = 0.0  #this is an example from last years code
        else:
            self.elevatorSpdCtrl.set(robotmap.elevator.elevatorHoldSpeed) #Add elevatorHoldSpeed to robotmap
            #self.elevatorLastSpeedSet = robotmap.elevator.elevatorHoldSpeed

# -----------------------------------------------------------------------------

    def rawMove(self, speed):
        self.elevatorSpdCtrl.set(speed)

    def move(self, speed):
        btmLimit = self.btmLimitSwitch.get()
        dist = self.elevatorEncoder.get()*robotmap.elevator.inchesPerTick
        topLimit = dist >= robotmap.elevator.elevatorMaxHeight
        if (btmLimit and speed <= 0.0) or (topLimit and speed > 0.0):
            self.elevatorSpdCtrl.set(robotmap.elevator.elevatorHoldSpeed)
        else:
            self.elevatorSpdCtrl.set(speed)
        self.elevatorLastSpeedSet = speed    

"""
    def elevatorMoveUp(self, speed):
        self.elevatorSpdCtrl.set(speed)
        #self.elevatorLastSpeedSet = speed

    def elevatorMoveDown(self, speed):
        if not self.btmLimitSwitch:
            self.elevatorSpdCtrl.set(speed)
            #self.elevatorLastSpeedSet = speed

        else:
            self.elevatorSpdCtrl.set(0.0)
            #self.elevatorLastSpeedSet = 0.0
"""

    def resetEncoders(self):
        self.elevatorEncoder.reset()