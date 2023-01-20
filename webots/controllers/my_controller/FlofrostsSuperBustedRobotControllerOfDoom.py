import Fmath
from controller import Robot,Motor

class FlofrostsSuperDuperRobotOfEpicnessThatWillTotallyWinTheSUperSmashBrosGame(Robot):
    
    __velocipy = Fmath.ComplexN(3,0)

    def __init__(self):
        super().__init__()

        self.__pitchMotor = Motor("body pitch motor")
        self.__yawMotor = Motor("body yaw motor")
        self.__yawSensor = self.__yawMotor.position_sensor()

        self.__pitchMotor.setPosition(float("inf"))
        self.__yawMotor.setPosition(float("inf"))

    def proceed(self):
        self.__pitchMotor.setVelocity(self.__velocipy.modulus)
        self.__yawMotor.setVelocity(self.__velocipy.angle)
        print(f"Speed : {self.__pitchMotor.getVelocity()}, Angle : {self.__yawSensor.getValue()}")