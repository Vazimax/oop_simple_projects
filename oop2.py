###### CLASS METHOD ######

from datetime import date
class Student():
    def __init__(self,fullname,age):
        self.name = fullname
        self.age = age

    def describing(self):
        print(f"Name : {self.name} , Age : {self.age} ")

    @classmethod
    def initFormBirthYear(cls,name,birthYear):
        return cls(name,date.today().year - birthYear)

student1 = Student('bakr',16)
student1.describing()
student2 = Student.initFormBirthYear('jhon',2000)
student2.describing()

class Pizza():
    def __init__(self,ingredients):
        self.ingredients = ingredients

    @classmethod
    def royal(cls):
        return cls(['fish','chicken','tomato','meat','chese'])
    
    @classmethod
    def veg(cls):
        return cls(['tomato','onion','olives'])

    def __str__(self):
        return str(self.ingredients)
    

pizza1 = Pizza(['meat','mushroom','tomato','olives'])
pizza2 = Pizza.royal()
pizza3 = Pizza.veg()

print(f'normal pizza : {pizza1} , royal pizza {pizza2} , vegeterian pizza {pizza3}')
