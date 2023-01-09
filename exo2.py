from exo1 import Robot

class Hooman:
    
    __belly = 500
    __maxBelly = 1000
    
    def __init__(self, gender):
        self.__sex = gender

    def __str__(self):
        return "\
                \rGender : {sex}\n\
                \rHunger : {hunger}% ({belly}g)\n\
            ".format(sex = "Male" if self.__sex else "Female",\
                     hunger = f"{int(self.__belly*100/self.__maxBelly):02d}",\
                     belly = self.__belly)
        
    def digest(self):
        self.__belly -= 42
        self.__belly = max(0,self.__belly)

    def eat(self, foods):
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
        self.digest()
        
    @property
    def sex(self):
        return self.__sex
        

class Food:

    mass = 0
    
    def __init__(self, mass):
        self.mass = mass
            
            
class Cyborg(Robot,Hooman):
    
    def __init__(self, name="romeo", gender = 0):
        Hooman.__init__(self, gender)
        Robot.__init__(self, name)

    def __str__(self):
        return Robot.__str__(self) + "\n" + Hooman.__str__(self)

    def fun(self):
        print("\
                \r         _____   \n\
                \r       /  ___  \ \n\
                \r     /  /  _  \  \ \n\
                \r   /( /( /(_)\ )\ )\ \n\
                \r  (  \  \ ___ /  /  ) \n\
                \r  (    \ _____ /    ) \n\
                \r  /(               )\ \n\
                \r |  \             /  | \n\
                \r |    \ _______ /    | \n\
                \r  \    / \   / \    / \n\
                \r    \/    | |    \/ \n\
                \r          | |  \n\
                \r          | | \n\
                \r          | | \n\
            ")

cyborg = Cyborg('Deux Ex Machina', 1)

print(cyborg.name, 'sexe', cyborg.sex)
print('Charging battery...')
cyborg.chargeBattery()
print(cyborg)
banana = Food(118); coca = Food(2000); chips = Food(340)
cyborg.eat(banana)
cyborg.eat([coca, chips])
print(cyborg)
cyborg.digest()
print(cyborg)
cyborg.fun()