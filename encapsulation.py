class person:
    def __init__(self,name,age):
        self.name = name
        self.__age = age  #private property
    def get_age(self):
        return self.__age
p1 = person("john",21)
print(p1.name)
print(p1.get_age())

class person:
    def __init__(self,name,age):
        self.name = name
        self.__age = age  #private property
    def get_age(self):
        return self.__age
    def set_age(self, age):
        if age>0:
            self.__age= age
        else:
            print("age must be positive")
p1 = person("john",21)
print(p1.name)
print(p1.get_age())
p1.set_age(29)
print(p1.get_age())

class person:
    def __init__(self,name,salary):
        self.name = name
        self._salary = salary  #private property
p1 = person("john",21000)
print(p1.name)
print(p1._salary)