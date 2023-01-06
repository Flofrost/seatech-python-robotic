import exo1

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
        

class Food:

    mass = 0
    
    def __init__(self, mass):
        self.mass = mass
            
            
class Cyborg(exo1.Robot,Hooman):
    
    def __init__(self, name="romeo"):
        super().__init__(name)

    def __str__(self):
        return super().__str__()

    def fun(self):
        pass


h = Hooman(0)
apple = Food(170)
tiramisu = Food(343)
print(h)
h.eat([apple,tiramisu])
print(h)
h.exist()
print(h)