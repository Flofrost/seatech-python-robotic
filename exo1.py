from time import sleep
from FlofrostsSuperClassStashOfEpicness import ComplexN
import math


class Robot():

    __powerState = 0
    __batteryLevel = 0
    __vector = ComplexN()
    __targetVector = ComplexN()

    def __init__(self, name="romeo"):
        self.name = name
        
    def __str__(self):
        return "\
            \rPower State : {power}\n\
            \rBattery Level : {battery}%\n\
            \rCurrent Velocity : {speed} m/s\n\
            \rCurrent Direction : {direction} deg\n\
            \r".format(\
                power = "On" if self.__powerState else "Off",\
                battery = self.__batteryLevel,\
                speed = self.__vector.modulus,\
                direction = self.__vector.angle * (180 / math.pi))
            
    def chargeBattery(self):
        while(self.__batteryLevel < 100):
            self.__batteryLevel += 1
            print("\rCharging... {}%   ".format(self.__batteryLevel),end="")
            sleep(0.1)
        print("Charging Complete!")
        
    def powerOn(self):
        if self.__batteryLevel:
            self.__powerState = 1
    
    def powerOff(self):
        self.stop()
        self.__powerState = 0
        
    def stop(self):
        self.__vector.modulus = 0
        
    def proceed(self):
        pass

    @property
    def speed(self):
        return self.__vector.modulus
    
    @speed.setter
    def speed(self,speed):
        if self.__powerState:
            self.__batteryLevel -= 5
            self.__vector.modulus = min(speed,300000000)
            
    @property
    def batteryLevel(self):
        return self.__batteryLevel

    @batteryLevel.setter
    def batteryLevel(self,batteryLevel):
        if batteryLevel < 0:
            self.__batteryLevel = 0
            self.powerOff()
        else:
            self.__batteryLevel = batteryLevel
            self.__batteryLevel = min(100,batteryLevel)
            
    @property
    def direction(self):
        return self.__vector
    
    @direction.setter
    def direction(self,direction:ComplexN):
        self.__vector = direction

if __name__ == '__main__':
    r = Robot("bob")

    r.speed = 65486
    print(r)
    r.chargeBattery()
    r.powerOn()
    r.speed = 50
    print(r)
