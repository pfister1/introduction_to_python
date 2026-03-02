# __init__() method
class User:
    def __init__(self, name, age, city, country):
     self.name = name
     self.age = age
     self.city = city
     self.country = country
user1 = User("peter",18,"nairobi","kenya")
print(user1.name)
print(user1.age)
print(user1.city)
print(user1.country)

class Cars:
   def __init__(my_object, brand, model, year):
      my_object.brand = brand
      my_object.model = model
      my_object.year = year
cars1 = Cars("bmw","m3",2024)
print(cars1.brand)
print(cars1.model)
print(cars1.year)

class person:
   def __init__(self,name,age):
      self.name = name
      self.age = age
   def greetings(self):
      print("hello, my name is" + self.name)
p1 = person("john",18)
p1.greetings()

class dog:
   def __init__(self,name,breed="pitbull"):
      self.name = name
      self.breed = breed
dog1 = dog("Shila")
dog2 = dog("ruby","shepherd")
print(dog1.name)
print(dog1.breed)
print(dog2.name)
print(dog2.breed)

class car:
   def __init__(self,brand,year):
      self.brand = brand
      self.year = year
   def dese(self):
      print("my car is" + self.brand)
car1 = car("audi",2013)
car1.dese()