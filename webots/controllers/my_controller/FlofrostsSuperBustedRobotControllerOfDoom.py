import Fmath
from controller import Robot,Motor,GPS,Accelerometer

arenaLim1 = [-4, -4]
arenaLim2 = [ 4,  4]

class FlofrostsSuperDuperRobotOfEpicnessThatWillTotallyWinTheSUperSmashBrosGame(Robot):
    
    __velocipy = Fmath.ComplexN(3,0)
    __currentPos = Fmath.ComplexN(0,0)
    __targetPos = Fmath.ComplexN(0,0)

    def __init__(self):
        super().__init__()

        self.__pitchMotor = Motor("body pitch motor")
        self.__yawMotor = Motor("body yaw motor")
        self.__pitchMotor.setPosition(float("inf"))
        self.__yawMotor.setPosition(float("inf"))

        self.__gps = GPS("gps")
        self.__gps.enable(int(self.getBasicTimeStep()))
        
        self.__accelerometer = Accelerometer("body accelerometer")
        self.__accelerometer.enable(int(self.getBasicTimeStep()))

    def __str__(self) -> str:
        return f"X: {self.__gps.value[0]:.2f}, Z: {self.__gps.value[1]:.2f}"


    def proceed(self):
        # Update position according to gps
        self.__currentPos = Fmath.ComplexN(self.__gps.value[0], self.__gps.value[1])
        
        self.__velocipy = self.__currentPos - self.__targetPos

        self.__pitchMotor.setVelocity(self.__velocipy.modulus)
        self.__yawMotor.setVelocity(self.__velocipy.angle)
        print(self)
