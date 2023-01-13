"""Projectile Class collection"""
from abc import ABCMeta, abstractmethod
from FlofrostsSuperClassStashOfEpicness import ComplexN

class Projectile(metaclass=ABCMeta):

    """Basic Projectile Template"""

    __position = ComplexN(0,0)
    __velocity = ComplexN(0,0)

    def __str__(self) -> str:
        return f"\nPosition : {self.__position}\nVelocity : {self.__velocity}\n"

    @abstractmethod
    def update_position(self):
        """Updates the position of the projectile"""


class Laser(Projectile):

    """Laser go pew and doesn't respect gravity"""

    def __init__(self, pos:ComplexN = ComplexN(0,0), vel:ComplexN = ComplexN(0,0)):
        """
        pos = Starting position of the laser
        vel = Velocity of the laser
        """
        self.__position = pos
        self.__velocity = vel

    def update_position(self):
        self.__position = self.__position + self.__velocity

class Arrow(Projectile):

    """Arrow goes stoing and respeccs gravity"""

    def __init__(self, pos:ComplexN = ComplexN(0,0), vel:ComplexN = ComplexN(0,0)):
        """
        pos = Starting position of the laser
        vel = Velocity of the laser
        """
        self.__position = pos
        self.__velocity = vel

    def update_position(self):
        self.__position = self.__position + self.__velocity
        self.__velocity.imaginary -= 1
