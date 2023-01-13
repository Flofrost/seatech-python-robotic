"""Yo mama"""
from exo1 import Robot


class Hooman:

    """A Human Lives"""

    __belly = 500
    __maxBelly = 1000

    def __init__(self, gender):
        self.__sex = gender

    def __str__(self):
        return f"   \rGender : {'Male' if self.__sex else 'Female'}\n\
                    \rHunger : {f'{int(self.__belly*100/self.__maxBelly):02d}'}% ({self.__belly}g)\n"

    def digest(self):
        """Digests food"""
        self.__belly -= 42
        self.__belly = max(0,self.__belly)

    def eat(self, foods):
        """CONSUME"""
        try:
            iter(foods)
        except TypeError:
            if self.__belly < self.__maxBelly and isinstance(foods, Food):
                self.__belly += foods.mass
        else:
            for food in foods:
                if self.__belly < self.__maxBelly and isinstance(food, Food):
                    self.__belly += food.mass
        self.__belly = min(self.__belly, self.__maxBelly)

    def exist(self):
        """life is pain"""
        self.digest()

    @property
    def sex(self):
        """Get the sex of the Hooman as a boolean"""
        return self.__sex


class Food:

    """Yum Yum"""

    mass = 0

    def __init__(self, mass):
        self.mass = mass


class Cyborg(Robot,Hooman):

    """both hooman and bobot"""

    def __init__(self, name="romeo", gender = 0):
        Hooman.__init__(self, gender)
        Robot.__init__(self, name)

    def __str__(self):
        return Robot.__str__(self) + "\n" + Hooman.__str__(self)

    def fun(self):
        """fuck you"""
        print("\
                \r         _____   \n\
                \r       /  ___  \\ \n\
                \r     /  /  _  \\  \\ \n\
                \r   /( /( /(_)\\ )\\ )\\ \n\
                \r  (  \\  \\ ___ /  /  ) \n\
                \r  (    \\ _____ /    ) \n\
                \r  /(               )\\ \n\
                \r |  \\             /  | \n\
                \r |    \\ _______ /    | \n\
                \r  \\    / \\   / \\    / \n\
                \r    \\/    | |    \\/ \n\
                \r          | |  \n\
                \r          | | \n\
                \r          | | \n\
            ")

if __name__ == "__main__":
    cyborg = Cyborg('Deux Ex Machina', 1)

    print(cyborg.name, 'sexe', cyborg.sex)
    print('Charging battery...')
    cyborg.chargeBattery()
    print(cyborg)
    banana = Food(118)
    coca = Food(2000)
    chips = Food(340)
    cyborg.eat(banana)
    cyborg.eat([coca, chips])
    print(cyborg)
    cyborg.digest()
    print(cyborg)
    cyborg.fun()
