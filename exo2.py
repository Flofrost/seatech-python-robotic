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
        pass

    def eat(self, foods):
        if isinstance(foods, Food):
            try:
                iter(foods)
            except TypeError:
                if self.__belly < 1000:
                    self.__belly += foods.mass
            else:
                for food in foods:
                    if self.__belly < 1000:
                        self.__belly += food.mass
                    
        
        def exist(self):
            self.digest()
        

class Food:

    mass = 0
    
    def __init__(self, mass):
        self.mass = mass
            

h = Hooman(0)
apple = Food(170)
print(h)
h.eat(apple)
print(h)