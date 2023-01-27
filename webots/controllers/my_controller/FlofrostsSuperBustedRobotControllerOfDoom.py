from Fmath import *
from controller import Robot,Motor,GPS,InertialUnit

arenaLim1 = [-4, -4]
arenaLim2 = [ 4,  4]

class FlofrostsSuperDuperRobotOfEpicnessThatWillTotallyWinTheSuperSmashBrosGame(Robot):
    
    __targetVel = ComplexN(3,0)
    __targetPos = ComplexN(0,0)
    
    __verboseMode = "log"

    def __init__(self):
        super().__init__()

        self.__pitchMotor = Motor("body pitch motor")
        self.__yawMotor = Motor("body yaw motor")
        self.__headMotor = Motor("head yaw motor")
        self.__pitchMotor.setPosition(float("inf"))
        self.__headMotor.setPosition(float("inf"))
        self.__yawMotor.setPosition(float("inf"))

        self.__gps = GPS("gps")
        self.__gps.enable(int(self.getBasicTimeStep()))
        
        self.__rotate = InertialUnit("rotateSensor")
        self.__rotate.enable(int(self.getBasicTimeStep()))

        if self.__verboseMode == "log":
            self.__logFile = open("log.csv", "w")
            self.__logFile.write("Pos X, Pos Z, angle (t-r)\n")
            
    def __del__(self):
        if self.__verboseMode == "log":
            self.__logFile.close()

    def __str__(self) -> str:
        if self.__verboseMode == "log":
            return f"{self.__gps.value[0]:.03f},\
                     {self.__gps.value[1]:.03f},\
                     {self.__angleError:.03f}\n".replace(" ","")

    def goTo(self,newTargetPosition:ComplexN):
        self.__targetPos = newTargetPosition

    def proceed(self):
        self.__targetVel = self.position - self.__targetPos
        self.__angleError = self.__targetVel.angle - self.__rotate.roll_pitch_yaw[2]

        self.__pitchMotor.setVelocity(self.__targetVel.modulus / max(self.__angleError, 1))
        self.__yawMotor.setVelocity(self.__targetVel.angle)

        # print(self.__rotate.roll_pitch_yaw)

        if self.__verboseMode == "log":
            self.__logFile.write(str(self))       
        
    @property
    def position(self) -> ComplexN:
        return ComplexN(self.__gps.value[0], self.__gps.value[1])
    
    @property
    def velocity(self) -> ComplexN:
        return ComplexN(self.__gps.speed_vector[0], self.__gps.speed_vector[1])
