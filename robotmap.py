import math
import wpilib


class ConfigHolder:
    """Dummy class to add config parameters too"""
    pass


# flag if we are at competition and want to use development features in the code
# Robot.init() will set this based on FMS being attached
devMode = False



# ----------------------------------------------------------
# Driveline Subsystem Config
# ----------------------------------------------------------
driveLine = ConfigHolder()
driveLine.leftMotorPort = 0
driveLine.rightMotorPort = 1
driveLine.frontIRPort = 8          
driveLine.backIRPort = 9          

# the new MecanumDrive library from WPILIP inverts the right motors by default, so inversion is often not needed.
# Be sure to view the wheel direction when moving side to side and forward/backward on mounts before testing on ground to verify
# and remember that the rollers on the wheels should form an X when looked at from the top/bottom
#  (ie right rear and left front wheels rolers are aligned in same direction, etc..)
driveLine.invertLeft = True
driveLine.invertRight = False
#driveLine.invertRightRear = False

# ----------------------------------------------------------
# Lift Subsystem Config
# ----------------------------------------------------------
lift = ConfigHolder()
lift.raiseBtnAll = 1

# ----------------------------------------------------------
# elevator Subsystem Config
# ----------------------------------------------------------

#reconfigure these ports
elevator = ConfigHolder()
elevator.btmLimitSwitchPort = 6     # DIO port
elevator.motorPort = 5      #???
elevator.btmLimitNormalClosed = False  # switch is wired to be normally cosed, so will return True when not tripped
elevator.holdSpeed = 0.2
elevator.elevatorDeadZone = .05
elevator.scaleSpdUp = 1.0
elevator.scaleSpdDown = 1.0

#reconfigure these ports
elevator.encAPort = 1
elevator.encBPort = 2
elevator.encType = wpilib.Encoder.EncodingType.k4X
elevator.encReverse = False
elevator.maxHeight = 48 #change once built, should be in inches since encoder measures ticks per inch

elevator.inchesPerTick = 0.1        #have to calculate this w/ radius once it is actually built
#drive wheel radius?

#---------------------------------------------------------------------------------------------
# ramp Subsystem Config
#---------------------------------------------------------------------------------------------
ramp = ConfigHolder()
ramp.solenoidPort1= 1
ramp.solenoidPort2= 2

# ----------------------------------------------------------
# General Sensors Config
# ----------------------------------------------------------
sensors = ConfigHolder()
sensors.hasAHRS = True

#------------------------------------------------------------
# Cargo Grab Config
#------------------------------------------------------------
cargograb = ConfigHolder()
cargograb.rightServoPort = 5 #Can be changed
cargograb.leftServoPort = 6 #Can be changed

print("RobotMap module completed load")

