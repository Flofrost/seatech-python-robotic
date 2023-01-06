from curses import setupterm
from operator import mod
from time import sleep
import math

class ComplexN():

    real = 0
    imaginary = 0
    
    def __init__(self,real = 0, imaginary = 0):
        self.real = real
        self.imaginary = imaginary
    
    @property
    def modulus(self):
        return math.sqrt(self.real ** 2 + self.imaginary ** 2)

    @modulus.setter
    def modulus(self, modulus):
        self.setPolar(modulus, self.angle)
    
    @property
    def angle(self):
        if self.real == 0:
            return math.pi / 2 if self.imaginary >= 0 else - math.pi / 2
        if self.real < 0:
            return math.atan(self.imaginary / self.real) + math.pi
        return math.atan(self.imaginary / self.real)
    
    @angle.setter
    def angle(self, angle):
        self.setPolar(self.modulus, angle)

    def setPolar(self, modulus, angle):
        self.real = modulus * math.cos(angle)
        self.imaginary = modulus * math.sin(angle)


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
            
    # @property
    # def direction(self):
    #     return self.__direction
    
    # @direction.setter
    # def direction(self,direction):
    #     self.__direction = direction % 360

if __name__ == '__main__':
    r = Robot("bob")

    r.speed = 65486
    print(r)
    r.chargeBattery()
    r.powerOn()
    r.speed = 50
    print(r)