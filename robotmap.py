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
driveLine.spdCompSmall = 1.0
driveLine.spdCompMedium = 1.0
driveLine.spdCompLarge = 1.0
driveLine.RtSensPort = 1      # Line detect analog input right-sensor port 
driveLine.LftSensPort = 2     # Line detect analog input left-sensor port

# the new MecanumDrive library from WPILIP inverts the right motors by default, so inversion is often not needed.
# Be sure to view the wheel direction when moving side to side and forward/backward on mounts before testing on ground to verify
# and remember that the rollers on the wheels should form an X when looked at from the top/bottom
#  (ie right rear and left front wheels rolers are aligned in same direction, etc..)
driveLine.invertLeft = True
driveLine.invertRight = False
#driveLine.invertRightRear = False

# ----------------------------------------------------------
# NFS Driving Config
# ----------------------------------------------------------
nfs = ConfigHolder()
nfs.debugTurning = False

"""
Turn scaling is used to reduce the maximum ammount of turn as the throttle increases to improve stability and
make the feel closer to that of driving a car

Heavy scalling is used while driving "slow", and lighter scaling is used during normal driving
Thus:
lowTurnScale -> normal driving
highTurnScale -> "slow" driving (while holding left trigger)

"""
nfs.lowTurnScale = 0.3                  # How much to reduce turn speed when driving at full throttle at
nfs.highTurnScale = 0.2
nfs.slowDriveSpeedFactor = 0.7          # Max speed when driving in slow mode

"""
minTimeFullThrottleChange
The minimum amount of time that the tank drive will allow the motors to switch from -1.0 to +1.0
Example: a value of 1 means that it will take 1 sec for the speed controllers to be updated from -1.0 to +1.0

The maximum speed controller change per periodic call is thus 
maxThrottleChange = totalThrottleRange (2) * callSpeed (0.02sec) / time (minTimeFullThrottleChange)

0.02 = 50 times per second (the updated packets to the robot
"""
nfs.minTimeFullThrottleChange = 1.5
nfs.maxSpeedChange = (2 * 0.02) / nfs.minTimeFullThrottleChange

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

#-----------------------------------------------------------
# Hatch Grab Config
#-----------------------------------------------------------
hatchgrab = ConfigHolder()
hatchgrab.solenoid=3