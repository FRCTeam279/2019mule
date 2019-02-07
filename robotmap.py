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
elevator = ConfigHolder() #must reconfigure the motorports
elevator.btmLimitSwitchPort = 6 # DIO port
elevator.elevatorMotorPort = 5 #???
elevator.elevatorBtmLimitNormalClosed = False  # switch is wired to be normally cosed, so will return True when not tripped

# ----------------------------------------------------------
# General Sensors Config
# ----------------------------------------------------------
sensors = ConfigHolder()
sensors.hasAHRS = True


print("RobotMap module completed load")

