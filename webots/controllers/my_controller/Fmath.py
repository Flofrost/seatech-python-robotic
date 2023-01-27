"""Contains cool stuff for the exercices"""
import math

def sigmoid(x, slope=1, offset=0):
    return 1 / (1 + math.exp(-slope * (x - offset)))

class ComplexN():

    """
    Complex Number implemented by Flofrost

    Contains a Real and Imaginary part
    Polar forms are always converted from and to Rectangular forms under the hood
    """

    real = 0
    imaginary = 0

    def __init__(self,real = 0, imaginary = 0, mode = 0):
        """
        'real' is the real part of the complex number
        'imaginary' is the imaginary part of the complex number
        
        If 'mode' is set, 'real" and 'imaginary' will be interprested as 'modulus' and 'angle' respectively
        """
        
        if not mode:
            self.real = real
            self.imaginary = imaginary
        else:
            self.setPolar(real,imaginary)
        
    def __str__(self) -> str:
        return f"{self.real} + {self.imaginary} j"
    
    def __add__(self, other):
        if type(other) is ComplexN:
            return ComplexN(self.real + other.real, self.imaginary + other.imaginary)
        raise Exception("Must add with other ComplexN")
    
    def __sub__(self, other):
        if type(other) is ComplexN:
            return ComplexN(self.real - other.real, self.imaginary - other.imaginary)
        raise Exception("Must substract with other ComplexN")
    
    def __mul__(self, other):
        if type(other) is ComplexN:
            return ComplexN(self.modulus * other.modulus, self.angle + other.angle, mode=1)
        elif type(other) is int or type(other) is float:
            return ComplexN(self.real * other, self.imaginary * other)
        raise Exception("Must multiply with another ComplexN or int or float")

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
        return math.atan(self.imaginary / self.real)

    @angle.setter
    def angle(self, angle):
        self.setPolar(self.modulus, angle)

    def setPolar(self, modulus, angle):
        """Sets the modulus and angle in one go"""
        self.real = modulus * math.cos(angle)
        self.imaginary = modulus * math.sin(angle)
        
    def dotProduct(self, other):
        if type(other) is ComplexN:
            return self.real * other.real + self.imaginary * self.imaginary
        raise Exception("Other must be ComplexN")
