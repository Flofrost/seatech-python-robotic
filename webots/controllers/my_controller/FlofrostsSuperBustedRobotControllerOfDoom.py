from tabnanny import verbose
import Fmath
from math import pi, cos
from controller import Robot,Motor,GPS,InertialUnit

arenaLim1 = [-4, -4]
arenaLim2 = [ 4,  4]

class FlofrostsSuperDuperRobotOfEpicnessThatWillTotallyWinTheSuperSmashBrosGame(Robot):
    
    __targetDir = Fmath.ComplexN(3,0)
    __targetPos = Fmath.ComplexN(0,0)
    
    __angleError = 0
    
    __verboseMode = "log"

    def __init__(self):
        super().__init__()

        self.__Lmotor = Motor("left wheel motor")
        self.__Lmotor.setPosition(float("inf"))
        self.__Rmotor = Motor("right wheel motor")
        self.__Rmotor.setPosition(float("inf"))

        self.__gps = GPS("gps")
        self.__gps.enable(int(self.getBasicTimeStep()))
        
        self.__rotate = InertialUnit("rotateSensor")
        self.__rotate.enable(int(self.getBasicTimeStep()))

        if self.__verboseMode == "log":
            self.__logFile = open("log.csv", "w")
            self.__logFile.write("Pos X, Pos Z, rotate, dirAngle, err\n")
            
    def __del__(self):
        if self.__verboseMode == "log":
            self.__logFile.close()

    def __str__(self) -> str:
        if self.__verboseMode == "log":
            return f"{self.__gps.value[0]:.03f},\
                     {self.__gps.value[1]:.03f},\
                     {self.angle:.03f},\
                     {self.__targetDir.angle:.03f},\
                     {self.__angleError:.03f}\n".replace(" ","")

    def goTo(self,newTargetPosition:Fmath.ComplexN):
        self.__targetPos = newTargetPosition

    def applySpeedVector(self, vector:Fmath.ComplexN):
        self.__Lmotor.setVelocity(vector.modulus * (cos(vector.angle) if vector.angle > 0 else 1))
        self.__Rmotor.setVelocity(vector.modulus * (cos(vector.angle) if vector.angle < 0 else 1))

    def proceed(self):
        self.__targetDir = self.position - self.__targetPos
        self.__angleError += (self.__targetDir.angle - self.angle) * 0.01
        
        self.applySpeedVector(Fmath.ComplexN(10, max(min(self.__angleError, pi/2), -pi/2) * -1, mode=1))

        print(self, self.__Lmotor.getVelocity(), self.__Rmotor.getVelocity())

        if self.__verboseMode == "log":
            self.__logFile.write(str(self))       
        
    @property
    def position(self) -> Fmath.ComplexN:
        return Fmath.ComplexN(self.__gps.value[0], self.__gps.value[1])
    
    @property
    def angle(self) -> float:
        return self.__rotate.roll_pitch_yaw[2]
    
    @property
    def velocity(self) -> Fmath.ComplexN:
        return Fmath.ComplexN(self.__gps.speed_vector[0], self.__gps.speed_vector[1])
