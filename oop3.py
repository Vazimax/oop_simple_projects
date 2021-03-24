###### STATIC METHOD ######
import math

class Math:
    @staticmethod
    def add(x,y):
        return x + y

    @staticmethod
    def add99(num):
        return + 99

    @staticmethod
    def add999(num):
        return num + 999

    @staticmethod
    def PI():
        return 3.14159


class Pizza:
    def __init__(self,ingredients,radius):
        self.radius = radius
        self.ingredients = ingredients

    def __str__(self):
        return f"The pizza ingredients are : {self.ingredients}"

    def area(self):
        return Pizza.circle_area(self.radius)

    @staticmethod
    def circle_area(r):
        return pow(r,2) * Math.PI()
      
p = Pizza(['chicken','chese','mushroom'],5)
print(p.area())
print(Pizza.circle_area(8))