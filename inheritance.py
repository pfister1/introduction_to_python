class person:
    def __init__(self,first_name,second_name):
        self.first_name = first_name
        self.second_name = second_name
    def printname(self):
        print(self.first_name,self.second_name)
p1 = person("john","doe")
p1.printname()

class student(person):
    pass

#inheritance -child class
class person:
    def __init__(self,first_name,second_name):
        self.first_name = first_name
        self.second_name = second_name
    def printname(self):
        print(self.first_name,self.second_name)
class student(person):
    pass
s1 = student("mike","olsen")
s1.printname()