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
<<<<<<< HEAD
driveLine.pdpCANid = 0          #pdp on CAN ID 0
driveLine.pcmCANid = 1          #pcm on CAN ID 1
=======

>>>>>>> ab50d658db9f6f6212742aae4dce6f5a00c194e2

# the new MecanumDrive library from WPILIP inverts the right motors by default, so inversion is often not needed.
# Be sure to view the wheel direction when moving side to side and forward/backward on mounts before testing on ground to verify
# and remember that the rollers on the wheels should form an X when looked at from the top/bottom
#  (ie right rear and left front wheels rolers are aligned in same direction, etc..)
driveLine.invertLeft = False
driveLine.invertRight = False
#driveLine.invertRightRear = False



# ----------------------------------------------------------
# General Sensors Config
# ----------------------------------------------------------
sensors = ConfigHolder()
sensors.hasAHRS = True


# ----------------------------------------------------------
# CAN Adress ID Config
# ----------------------------------------------------------
canId = ConfigHolder
canId.Pcm = 1
canId.Pdb = 0


print("RobotMap module completed load")

