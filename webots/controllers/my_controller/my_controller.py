"""my_controller controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot
from FlofrostsSuperBustedRobotControllerOfDoom import *

robot = FlofrostsSuperDuperRobotOfEpicnessThatWillTotallyWinTheSUperSmashBrosGame()

# get the time step of the current world.
timestep = int(robot.getBasicTimeStep())


while robot.step(timestep) != -1: # Main Loop

    robot.proceed()    
