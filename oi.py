import math
from wpilib.joystick import Joystick
from wpilib.buttons.joystickbutton import JoystickButton
from commands.extendall import ExtendAll
from commands.retractall import RetractAll
from commands.extendfront import ExtendFront
from commands.extendback import ExtendBack
from commands.retractfront import RetractFront
from commands.rampextend import RampExtend
from commands.rampretract import RampRetract
import robotmap


class T16000M(Joystick):
    def __init__(self, port):
        super().__init__(port)
        self.port = port
        self.setXChannel(0)
        self.setYChannel(1)
        self.setZChannel(2)
        self.setThrottleChannel(3)
        self.setTwistChannel(2)


# ----------------------------------------------------------
# Config Values
# ----------------------------------------------------------

class ConfigHolder:
    pass


config = ConfigHolder()

# Driver Sticks
config.leftDriverStickNullZone = 0.1
config.rightDriverStickNullZone = 0.08

config.throttleFilterPower = 0.4
config.turnFilterPower = 0.4

# Left Joystickc
config.btnDriveSlow = 1
config.btnResetEncodersIndex = 2
config.btnEnableLightSensorIndex = 3

# Right Joystick
config.btnResetYawAngleIndex = 7 #temporarily changed from 2 to 7
config.btnExtendAllIndex = 1
config.btnRetractAllIndex = 2
config.btnExtendFrontIndex = 3
config.btnExtendBackIndex = 4
config.btnRetractFrontIndex = 5
config.btnRetractBackIndex = 6

# GO Gamepad (Logitech)
config.btnHatchGrabTogIndex = 1    # 1 = A
config.btnCargoGrabOpenTogIndex = 3    # 3 = X
config.btnCargoGrabCloseTogIndex = 5 #????
config.btnRampExtendTogIndex = 6
config.btnRampRetractTogIndex = 7

config.axisElevatorIndex = 9 #???

# ----------------------------------------------------------
# Stick and Button Objects
# ----------------------------------------------------------

leftDriverStick = None
rightDriverStick = None
goGamePad = None
resetYawBtn = None
btnResetEncoders = None
btnDriveSlow = None
btnLift = None             # added to eject/retract cylinder(s)
btnRetract = None
btnEnableLightSensor = None

btnRampExtendTog = None
btnRampRetractTog = None 
btnHatchGrabTog = None
btnCargoGrabTog = None
axisElevator = None

# ----------------------------------------------------------
# Init
# ----------------------------------------------------------


def init():
    """
    Assign commands to button actions, and publish your joysticks so you
    can read values from them later.
    """

    global leftDriverStick
    global rightDriverStick
    global goGamePad

    try:
        leftDriverStick = T16000M(0)
    except:
        print('OI: Error - Could not instantiate Left Driver Stick on USB port 0!!!')

    try:
        rightDriverStick = T16000M(1)
    except:
        print('OI: Error - Could not instantiate Right Driver Stick on USB port 0!!!')

    try:
        goGamePad = Joystick(2)
    except:
        print('OI: Error - Could not instantiate Right Driver Stick on USB port 2!!!')


    # ----------------------------------------------------------
    # Driver Controls
    # ----------------------------------------------------------
    #global resetYawBtn
    #resetYawBtn = JoystickButton(rightDriverStick, config.btnResetYawAngleIndex)
    #resetYawBtn.whenPressed(NavxResetYawAngle())

    global btnDriveSlow
    btnDriveSlow = JoystickButton(leftDriverStick, config.btnDriveSlow)
    
    global btnEnableLightSensor
    btnEnableLightSensor = JoystickButton(leftDriverStick, config.btnEnableLightSensorIndex)

    global btnExtendAll
    btnExtendAll = JoystickButton(rightDriverStick, config.btnExtendAllIndex)
    btnExtendAll.whenPressed(ExtendAll())

    global btnRetract
    btnRetract = JoystickButton(rightDriverStick, config.btnRetractAllIndex)
    btnRetract.whenPressed(RetractAll())

    global btnExtendFront
    btnExtendFront = JoystickButton(rightDriverStick, config.btnExtendFrontIndex)
    btnExtendFront.whenPressed(ExtendFront())

    global btnExtendBack
    btnExtendBack = JoystickButton(rightDriverStick, config.btnExtendBackIndex)
    btnExtendBack.whenPressed(ExtendBack())

    global btnRetractFront
    btnRetractFront = JoystickButton(rightDriverStick, config.btnRetractFrontIndex)
    btnRetractFront.whenPressed(RetractFront())

    global btnCargoGrabTog
    btnCargoGrabTog = JoystickButton(goGamePad, config.btnHatchGrabTogIndex)
    btnCargoGrabTog.whenPressed(ExtendBack())
    
    """
    global btnResetEncoders
    btnResetEncoders = JoystickButton(leftDriverStick, config.btnResetEncodersIndex)
    btnResetEncoders.whenPressed(TankDriveResetEncoders())
    """

    """
    global axisElevator
    axisElevator = JoystickAxis(goGamePad, config.axisElevatorIndex)
    axisElevator.     #??? idk how to configure joystick axis
    """

    """
    global btnRampTog
    btnRampTog = JoystickButton(goGamePad, config.btnRampTogIndex)
    btnRampTog.whenPressed(ExtendFront())
    """
    #global btnResetEncoders
    #btnResetEncoders = JoystickButton(leftDriverStick, config.btnResetEncodersIndex)
    #btnResetEncoders.whenPressed(TankDriveResetEncoders())

    # These variable names are inconsistent, need to be fixed!!!!
    #global btnRampExtendTog
    #btnRampExtendTog = JoystickButton(goGamePad, config.btnRampExtendTogIndex)
    #btnRampExtendTog.whenPressed(RampExtend())

    #global btnRampRetractTog
    #btnRampRetractTog = JoystickButton(goGamePad, config.btnRampRetractTogIndex)
    #btnRampRetractTog.whenPressed(RampRetract())

# ----------------------------------------------------------
# Utility Functions
# ----------------------------------------------------------

# https://www.desmos.com/calculator/yopfm4gkno
# power should be > 0.1 and less than 4 or 5 ish on the outside
#    If power is < 1.0, the curve is a logrithmic curve to give more power closer to center
#    Powers greater than one give a more traditional curve with less sensitivity near center
def filterInputToPower(val, deadZone=0.0, power=2):
    power = math.fabs(power)
    if power < 0.1:
        power = 0.1
    if power > 5:
        power = 5

    sign = 1.0
    if val < 0.0:
        sign = -1.0

    val = math.fabs(val)
    deadZone = math.fabs(deadZone)

    if val < deadZone:
        val = 0.0
    else:
        val = val * ((val - deadZone) / (1 - deadZone))

    output = val ** power
    return output * sign


# View output: https://www.desmos.com/calculator/uh8th7djep
# to keep a straight line, scale = 0, and filterFactor = 1
# Keep filterFactor between 0 and 1
# Scale can go from 0 up, but values over 3-4 have dubious value
# Nice curve for game pad is filterFactor = 0.2, scale=1.5
def filterInput(val, deadZone=0.0, filterFactor=1.0, scale=0.0):
    """
    Filter an input using a curve that makes the stick less sensitive at low input values
    Take into account any dead zone required for values very close to 0.0
    """

    sign = 1.0
    if val < 0.0:
        sign = -1.0

    val = math.fabs(val)
    deadZone = math.fabs(deadZone)

    if val < deadZone:
        val = 0.0
    else:
        val = val * ((val - deadZone) / (1 - deadZone))

    output = val * ((filterFactor * (val**scale)) + ((1 - filterFactor) * val))
    output *= sign
    return output
    #try using tanh with import numpy for a different scaling.


def applyDeadZone(val, deadZone):
    """
    Apply a dead zone to an input with no other smoothing. Values outsize the dead zone are correctly scaled for 0 to 1.0
    :return:
    The float value of the adjusted intput
    """
    sign = 1.0
    if val < 0.0:
        sign = -1.0

    val = math.fabs(val)
    deadZone = math.fabs(deadZone)

    if val < deadZone:
        val = 0.0
    else:
        val = val * ((val - deadZone) / (1 - deadZone))

    val *= sign
    return val


def getRawThrottle():
    """
    Use the Y Axis of the left stick for throttle.  Value is reversed so that 1.0 is forward (up on a joystick is usually negative input)
    :return:
    The float value of the throttle between -1.0 and 1.0
    """
    val = leftDriverStick.getY()
    if val != 0.0:
        val *= -1.0
    return val


def getRawTurn():
    return rightDriverStick.getX()

