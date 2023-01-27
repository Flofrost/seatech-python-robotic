import Fmath
from math import pi
from random import random
from controller import Robot,Motor,GPS,InertialUnit

arenaLim1 = [-4, -4]
arenaLim2 = [ 4,  4]

class FlofrostsSuperDuperRobotOfEpicnessThatWillTotallyWinTheSuperSmashBrosGame(Robot):
    
    __targetDir = Fmath.ComplexN(3,0)
    __targetPos = Fmath.ComplexN(0,0)
    
    __angleErrorPID = [0, 0, 0]
    
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
            self.__logFile.write("Pos X, Pos Z, rotate, dirAngle, P, I\n")
            
    def __del__(self):
        if self.__verboseMode == "log":
            self.__logFile.close()

    def __str__(self) -> str:
        if self.__verboseMode == "log":
            return f"{self.__gps.value[0]:.03f},\
                     {self.__gps.value[1]:.03f},\
                     {self.angle:.03f},\
                     {self.__targetDir.angle:.03f},\
                     {self.__angleErrorPID[0]:.03f},\
                     {self.__angleErrorPID[1]:.03f}\n".replace(" ","")

    def goTo(self,newTargetPosition:Fmath.ComplexN):
        self.__targetPos = newTargetPosition

    def applySpeedVector(self, vector:Fmath.ComplexN):
        offset = pi/4
        slope = 3.74
        self.__Lmotor.setVelocity(min(16, max(-16, vector.modulus * (Fmath.sigmoid(vector.angle, slope=-slope, offset=-offset) * 2 - 1))))
        self.__Rmotor.setVelocity(min(16, max(-16, vector.modulus * (Fmath.sigmoid(vector.angle, slope= slope, offset= offset) * 2 - 1))))

    def proceed(self):
        self.__targetDir = self.__targetPos - self.position
        angleError = self.__targetDir.angle - self.angle
        self.__angleErrorPID[0] =  angleError * 1
        self.__angleErrorPID[1] += angleError * (1 / 50)
        
        correctionVelocity = Fmath.ComplexN(self.__targetDir.modulus * 10,
                                            self.__angleErrorPID[0] + self.__angleErrorPID[1],
                                            mode=1)
        correctionVelocity.modulus *= max(0, correctionVelocity.dotProduct(self.__targetDir))
        self.applySpeedVector(correctionVelocity)

        # print(self, self.__Lmotor.getVelocity(), self.__Rmotor.getVelocity())

        if self.__targetDir.modulus < 0.3:
            self.__targetPos.real = random() * 8 - 4
            self.__targetPos.imaginary = random() * 8 - 4
            print(f"Changing target to position {self.__targetPos} !!")

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
