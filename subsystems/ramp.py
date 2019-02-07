import math
import wpilib
from wpilib.command.subsystem import Subsystem
from wpilib.doublesolenoid import DoubleSolenoid
from wpilib.digitalinput import DigitalInput

import subsystems
import robotmap

class Ramp(subsystem):
    print("Ramp: init called")
    super().__init__('Ramp')
    self.logPrefix= 'Ramp: '


