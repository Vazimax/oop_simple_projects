###### INSTANCE METHOD ######

class Student():
    NOS = 0
    def __init__(self,fullname,age,courses=None):
        self.__name = fullname
        self.__age = age
        self.__courses = courses
        Student.NOS += 1
    
    # Encapsulation

    def get_name(self):
        return self.__name
    def set_name(self , new_name):
        self.__name = new_name
    
    def get_age(self):
        return self.__age
    def set_age(self , new_age):
        self.__age = new_age

    def describing(self):
        print(f"Name : {self.__name} , Age : {self.__age} , Courses : {self.__courses}")

    def is_old(self):
        if self.__age >= 50 :
            print('The student is old :)')
        else :
            print('The student is not old =)')


student1 = Student('bakr habti',16,['math','pc','eng','cn','cs','ml'])
student2 = Student('jack wing',17,['math','bio','eng','cn','cs','ml'])
student3 = Student('marie tiara',16,['math','pc','fr','cn','cs','ml'])
student4 = Student('jiang yung',57,['math','pc','eng','cn','cs','dl','ml'])

student1.set_name('bakr el habti')
student1.set_age('17')
student1.describing()   




