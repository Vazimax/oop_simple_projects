class Human:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __add__(self,other):
        names = self.name + ' and ' + other.name
        ages  = self.age + other.age

        return f"names combined are : {names} , and the sum of the ages is : {ages}"

    def __lt__(self,other):
        return self.age > other.age

    def display(self):
        return f"Name : {self.name} , Age : {self.age}"

human1 = Human('bakr',16)
human2 = Human('sofie',16)
print(human1+human2)
print(human2<human1)