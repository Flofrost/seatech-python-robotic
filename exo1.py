from time import sleep

class Robot():

    powerState = 0
    __batteryLevel = 0
    speed = 0

    def __init__(self, name="romeo"):
        self.name = name
        
    def __str__(self):
        return "\
            \rPower State : {power}\n\
            \rBattery Level : {battery}\n\
            \rCurrent Velocity : {speed}\n\
            \r".format(\
                power="none",\
                battery=str(self.__batteryLevel)+"%",\
                speed="none")
            
    def chargeBattery(self):
        while(self.__batteryLevel < 100):
            self.__batteryLevel += 1
            sleep(0.1)

r = Robot("bob")

print(r)
r.chargeBattery()
print(r)