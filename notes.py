# object oriented programming

# (define-struct dog [fur_color name age favorite_food])

class Dog:
    def __init__(self, name, age):
        pass
    def __str__(self):
        s = f"{self.name} is {self.age}years old"
        
logan = Dog("logan", 8)
becker = Dog("becker", 4)
kepa = Dog("kepa", 4)