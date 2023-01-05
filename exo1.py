from time import sleep

class Robot():

    __powerState = 0
    __batteryLevel = 0
    __speed = 0

    def __init__(self, name="romeo"):
        self.name = name
        
    def __str__(self):
        return "\
            \rPower State : {power}\n\
            \rBattery Level : {battery}%\n\
            \rCurrent Velocity : {speed} m/s\n\
            \r".format(\
                power="On" if self.__powerState else "Off",\
                battery=self.__batteryLevel,\
                speed=self.__speed)
            
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
        self.__speed = 0

    @property
    def speed(self):
        return self.__speed
    
    @speed.setter
    def speed(self,speed):
        if self.__powerState:
            self.__batteryLevel -= 5
            self.__speed = min(speed,300000000)
            
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

r = Robot("bob")

r.speed = 65486
print(r)
r.chargeBattery()
r.powerOn()
r.speed = 50
print(r)