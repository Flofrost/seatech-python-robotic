import Fmath
from controller import Robot,Motor,GPS,Accelerometer

class FlofrostsSuperDuperRobotOfEpicnessThatWillTotallyWinTheSUperSmashBrosGame(Robot):
    
    __velocipy = Fmath.ComplexN(3,0)

    def __init__(self):
        super().__init__()

        self.__pitchMotor = Motor("body pitch motor")
        self.__yawMotor = Motor("body yaw motor")
        self.__pitchMotor.setPosition(float("inf"))
        self.__yawMotor.setPosition(float("inf"))

        self.__gps = GPS("gps")
        self.__gps.enable(100)
        
        self.__accelerometer = Accelerometer("body accelerometer")
        self.__accelerometer.enable(100)

    def proceed(self):
        self.__pitchMotor.setVelocity(self.__velocipy.modulus)
        self.__yawMotor.setVelocity(self.__velocipy.angle)
        print(f"GPS : {self.__gps.value}, Accel : {self.__accelerometer.value}")