# Contains no juice

import wpilib
from commandbased import CommandBasedRobot
from wpilib.command import Scheduler
from wpilib import SmartDashboard
from wpilib.driverstation import DriverStation


# import items in the order they should be initialized to avoid any surprises
import robotmap
import subsystems
import oi

autoManager = None


class MyRobot(CommandBasedRobot):

    def robotInit(self):
        print('Robot Base - robotInit called')

        # subsystems must be initialized before things that use them
        # ensure order of operations is correct, just like importing to avoid issues with dependencies
        subsystems.init()
        oi.init()


    def autonomousInit(self):
        super().autonomousInit()

    def autonomousPeriodic(self):
        super().autonomousPeriodic()
        # optionally do stuff like display data to smart dashboard here while in autonomous

    def teleopPeriodic(self):
        Scheduler.getInstance().run()
        #optionally do stuff like display data to smart dashboard here while in teleop

    def disabledPeriodic(self):
        Scheduler.getInstance().run()
        # optionally do stuff like display data to smart dashboard here while in disabled


    def testPeriodic(self):
        wpilib.LiveWindow.run()
        # optionally do stuff like display data to smart dashboard here while in test


if __name__ == '__main__':
    wpilib.run(MyRobot)

