from datetime import date
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def display(self):
        return f"Name : {self.name} , Age : {self.age}"

    @classmethod
    def initFromBirthYear(cls,name,birth_year,extra):
        return cls(name,date.today().year - birth_year , extra)

class Woman(Person):
    gender = 'Female'
    NOW = 0

    def __init__(self,name,age,body):
        super().__init__(name,age)
        self.body = body
        Woman.NOW += 1
    
    def display(self):
        string = super().display()
        return string + f" , Gender : {self.gender} , Body : {self.body}"

class Man(Person):
    gender = 'Male'
    NOW = 0

    def __init__(self,name,age,body):
        super().__init__(name,age)
        self.body = body
        Woman.NOW += 1
    
    def display(self):
        string = super().display()
        return string + f", Gender : {self.gender} , Body : {self.body}"


woman1 = Woman.initFromBirthYear('Emilia',2004,'Mesomorph')
print(woman1.display())