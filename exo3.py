"""Projectile Class collection"""
from os import get_terminal_size
from time import sleep
from abc import ABCMeta, abstractmethod
from FlofrostsSuperClassStashOfEpicness import ComplexN

class Projectile(metaclass=ABCMeta):

    """Basic Projectile Template"""

    def __init__(self, pos:ComplexN = ComplexN(0,0), vel:ComplexN = ComplexN(0,0)) -> None:
        """
        pos = Starting position of the laser
        vel = Velocity of the laser
        """
        self.__position = pos
        self.__velocity = vel
        self.icon = "."

    def __str__(self) -> str:
        return f"\nPosition : {self.__position}\nVelocity : {self.vel}\n"

    @abstractmethod
    def updatePosition(self):
        """Updates the position of the projectile"""

    @abstractmethod
    def collisionDetection(self, map):
        """Detects weather the ptojectile has collided with a wall"""

    @property
    def pos(self):
        """coordinates of the projectile"""
        return self.__position
    
    @pos.setter
    def pos(self,pos:ComplexN):
        self.__position = pos

    @property
    def vel(self):
        """velocity of the projectile"""
        return self.__velocity
    
    @vel.setter
    def vel(self,vel:ComplexN):
        self.__velocity = vel

class Laser(Projectile):

    """Laser go pew and doesn't respect gravity"""

    def __init__(self, pos: ComplexN = ComplexN(0, 0), vel: ComplexN = ComplexN(0, 0)) -> None:
        super().__init__(pos, vel)
        self.icon = "+"

    def updatePosition(self):
        self.pos = self.pos + self.vel

    def collisionDetection(self, map):
        pass

class Arrow(Projectile):

    """Arrow goes stoing and respeccs gravity"""

    def __init__(self, pos: ComplexN = ComplexN(0, 0), vel: ComplexN = ComplexN(0, 0)) -> None:
        super().__init__(pos, vel)
        self.icon = ">"

    def updatePosition(self):
        self.pos = self.pos + self.vel
        self.vel.imaginary += 1

    def collisionDetection(self, map):
        pass


class LightArrow(Laser,Arrow):
    
    """Bounes and Arcs"""

    def __init__(self, pos: ComplexN = ComplexN(0, 0), vel: ComplexN = ComplexN(0, 0)) -> None:
        super().__init__(pos, vel)
        self.icon = "~"
        
    def updatePosition(self):
        Arrow.updatePosition(self)
        
    def collisionDetection(self, map):
        Laser.collisionDetection(self, map)

if __name__ == "__main__":

    wallBottom = 0.8
    wallRight = 0.9

    projList = [Laser(pos=ComplexN(10,10), vel=ComplexN(1,0)), Arrow(pos=ComplexN(10,12), vel=ComplexN(3,-3))]

    while True:
        print("\x1bc",end="") # clear term
        pos = get_terminal_size().columns
        y = get_terminal_size().lines

        frame = [[ "#" if i/pos > wallRight or j/y > wallBottom else " " for i in range(pos) ] for j in range(y)]
        
        rmvLst = []
        for proj in projList:
            proj.updatePosition()
            frame[proj.pos.imaginary][proj.pos.real] = proj.icon
            

        for line in frame:
            print("".join(line))

        sleep(0.33)
