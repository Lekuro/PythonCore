# Classy Classes
# Basic Classes, this kata is mainly aimed at the new JS ES6 Update introducing classes
# Task
# Your task is to complete this Class, the Person class has been created.
# You must fill in the Constructor method to accept a name as string and an age as number,
# complete the get Info property and getInfo method/Info getter which should return johns age is 34

class Person:

    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        # self.info = f"{name}'s age is {age}."

    @property
    def info(self):
        return f"{self.__name}'s age is {self.__age}."

    @info.setter
    def info(self, param):
        self.__name, self.__age = param

    # def getInfo(self):
    #     return self.info


p = Person('Sam', 12)
print(p.info)
p.info = 'Bob', 3
print(p.info)
# print(Person('Sam', 12).getInfo())
