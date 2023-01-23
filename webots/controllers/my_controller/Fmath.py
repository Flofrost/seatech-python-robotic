"""Contains cool stuff for the exercices"""
import math

class ComplexN():

    """
    Complex Number implemented by Flofrost

    Contains a Real and Imaginary part
    Polar forms are always converted from and to Rectangular forms under the hood
    """

    real = 0
    imaginary = 0

    def __init__(self,real = 0, imaginary = 0):
        self.real = real
        self.imaginary = imaginary
        
    def __str__(self) -> str:
        return f"{self.real} + {self.imaginary} j"
    
    def __add__(self, other):
        return ComplexN(self.real + other.real, self.imaginary + other.imaginary)
    
    def __sub__(self, other):
        return ComplexN(self.real - other.real, self.imaginary - other.imaginary)

    @property
    def modulus(self):
        """Modulus of the complex number"""
        return math.sqrt(self.real ** 2 + self.imaginary ** 2)

    @modulus.setter
    def modulus(self, modulus):
        self.setPolar(modulus, self.angle)

    @property
    def angle(self):
        """Angle in radians of the complex number"""
        if self.real == 0:
            return math.pi / 2 if self.imaginary >= 0 else - math.pi / 2
        if self.real < 0:
            return math.atan(self.imaginary / self.real) + math.pi
        return math.atan(self.imaginary / self.real)

    @angle.setter
    def angle(self, angle):
        self.setPolar(self.modulus, angle)

    def setPolar(self, modulus, angle):
        """Sets the modulus and angle in one go"""
        self.real = modulus * math.cos(angle)
        self.imaginary = modulus * math.sin(angle)
