import Fmath
from math import pi
from random import random
from controller import Robot,Motor,GPS,InertialUnit

arenaLim1 = [-4, -4]
arenaLim2 = [ 4,  4]

class FlofrostsSuperDuperRobotOfEpicnessThatWillTotallyWinTheSuperSmashBrosGame(Robot):
    
    __targetDir = Fmath.ComplexN(3,0)
    __targetPos = Fmath.ComplexN(0,0)
    
    __pid = [0, 0, 0]
    __prev = 0
    
    __verboseMode = "log"
    __robot = "bb8"

    def __init__(self):
        super().__init__()

        if self.__robot == "roomba":
            self.__Lmotor = Motor("left wheel motor")
            self.__Lmotor.setPosition(float("inf"))
            self.__Rmotor = Motor("right wheel motor")
            self.__Rmotor.setPosition(float("inf"))
        elif self.__robot == "bb8":
            self.__Lmotor = Motor("body pitch motor")
            self.__Lmotor.setPosition(float("inf"))
            self.__Rmotor = Motor("body yaw motor")
            self.__Rmotor.setPosition(float("inf"))
            self.__Rmotor.setVelocity(0)

        self.__gps = GPS("gps")
        self.__gps.enable(int(self.getBasicTimeStep()))
        
        self.__rotate = InertialUnit("rotateSensor")
        self.__rotate.enable(int(self.getBasicTimeStep()))

        if self.__verboseMode == "log":
            self.__logFile = open("log.csv", "w")
            self.__logFile.write("Wel L, Wel R, rotate, dirAngle, Err P, Err I\n")
            
    def __del__(self):
        if self.__verboseMode == "log":
            self.__logFile.close()

    def __str__(self) -> str:
        if self.__verboseMode == "log":
            return f"{self.__Lmotor.getVelocity():.03f},\
                     {self.__Rmotor.getVelocity():.03f},\
                     {self.angle:.03f},\
                     {self.__targetDir.angle:.03f},\
                     {self.__pid[0]:.03f},\
                     {self.__pid[1]:.03f}\n".replace(" ","")

    def goTo(self,newTargetPosition:Fmath.ComplexN):
        self.__targetPos = newTargetPosition

    def applySpeedVector(self, vector:Fmath.ComplexN):
        offset = pi/2
        slope = 3.74
        self.__Rmotor.setVelocity(max(-16, min(16, vector.modulus * (Fmath.sigmoid(vector.angle, slope=-slope, offset= offset) * 2 - 1))))
        self.__Lmotor.setVelocity(max(-16, min(16, vector.modulus * (Fmath.sigmoid(vector.angle, slope= slope, offset=-offset) * 2 - 1))))

    def proceed(self):
        self.__targetDir = self.__targetPos - self.position
        self.__angleError = self.__targetDir.angle - self.angle
        self.__pid[0] = self.__angleError * -1.5
        self.__pid[1] += self.__angleError * 0
        
        if self.__robot == "roomba":
            correctionVelocity = Fmath.ComplexN(-self.__targetDir.modulus * 1,
                                                10 if self.__angleError < 0 else -10,
                                                mode=1)
            correctionVelocity.modulus *= max(0, correctionVelocity.dotProduct(self.__targetDir))
            self.applySpeedVector(correctionVelocity)
        elif self.__robot == "bb8":
            self.__Lmotor.setVelocity(self.__targetDir.modulus * 2)
            self.__Rmotor.setVelocity(self.__targetDir.angle * 3)

        # print(self, self.__Lmotor.getVelocity(), self.__Rmotor.getVelocity())

        if self.__targetDir.modulus < 0.3:
            self.__targetPos.real = random() * 5 - 2.5
            self.__targetPos.imaginary = random() * 5 - 2.5
            print(f"Changing target to position {self.__targetPos} !!")

        if self.__verboseMode == "log":
            self.__logFile.write(str(self))       

        self.__prev = self.__angleError
        
    @property
    def position(self) -> Fmath.ComplexN:
        return Fmath.ComplexN(self.__gps.value[0], self.__gps.value[1])
    
    @property
    def angle(self) -> float:
        if self.__robot == "roomba":
            return self.__rotate.roll_pitch_yaw[2]
        elif self.__robot == "bb8":
            return self.__rotate.roll_pitch_yaw[2]
    
    @property
    def velocity(self) -> Fmath.ComplexN:
        return Fmath.ComplexN(self.__gps.speed_vector[0], self.__gps.speed_vector[1])
