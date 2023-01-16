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
        self.life = 50

    def updatePosition(self):
        self.pos = self.pos + self.vel
        self.life -= 1

    def collisionDetection(self, map):
        if map[int(self.pos.imaginary)][int(self.pos.real + self.vel.real)] == "#":
            self.vel.real *= -1
        if map[int(self.pos.imaginary + self.vel.imaginary)][int(self.pos.real)] == "#":
            self.vel.imaginary *= -1
        if self.life < 0:
            return 1
        return 0

class Arrow(Projectile):

    """Arrow goes stoing and respeccs gravity"""

    def __init__(self, pos: ComplexN = ComplexN(0, 0), vel: ComplexN = ComplexN(0, 0)) -> None:
        super().__init__(pos, vel)
        self.icon = ">"

    def updatePosition(self):
        self.pos = self.pos + self.vel
        self.vel.imaginary += 1
        if self.vel.modulus > 5:
            self.vel.modulus = 5

    def collisionDetection(self, map):
        if map[int(self.pos.imaginary)][int(self.pos.real + self.vel.real)] == "#":
            return 1
        if map[int(self.pos.imaginary + self.vel.imaginary)][int(self.pos.real)] == "#":
            return 1
        return 0


class LightArrow(Laser,Arrow):
    
    """Bounes and Arcs"""

    def __init__(self, pos: ComplexN = ComplexN(0, 0), vel: ComplexN = ComplexN(0, 0)):
        Laser.__init__(self, pos, vel)
        self.icon = "~"
        
    def updatePosition(self):
        Arrow.updatePosition(self)
        self.life -= 1
        
    def collisionDetection(self, map):
        return Laser.collisionDetection(self, map)

if __name__ == "__main__":

    wallBottom = 0.8
    wallRight = 0.9

    projList = [Laser(pos=ComplexN(20,10), vel=ComplexN(2,0)), Arrow(pos=ComplexN(10,12), vel=ComplexN(3,-3)), LightArrow(pos=ComplexN(5,20), vel=ComplexN(4,-4))]

    while projList:
        print("\x1bc",end="") # clear term
        pos = get_terminal_size().columns
        y = get_terminal_size().lines

        frame = [[ "#" if i/pos > wallRight or j/y > wallBottom else " " for i in range(pos) ] for j in range(y)]
        
        rmvLst = []
        for proj in projList:
            proj.updatePosition()
            frame[int(proj.pos.imaginary)][int(proj.pos.real)] = proj.icon
            if proj.collisionDetection(frame):
                rmvLst.append(proj)
        
        for rmv in rmvLst:
            projList.remove(rmv)

        for line in frame:
            print("".join(line))

        sleep(0.33)

    print("No more :)")
