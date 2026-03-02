x = "hello world"
print(len(x))

this_dict = {
    "brand":"ford",
    "model":"mustang",
    "year":"2016"
}
print(len(this_dict))

#classes are car, boat and plane
#method is move()
class car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    def move(self):
        print("drive")
class boat:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    def move(self):
        print("sail")   
class plane:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    def move(self):
        print("fly")
car1 = car("audi","q5")
boat1 = boat("sailer100","idk")
plane1 = plane("airways","2030")
for x in (car1,boat1,plane1):
    x.move()

class vehicle:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    def move(self):
        print("move")
class car(vehicle):
    pass
class boat(vehicle):
    def move(self):
        print("sail")
class plane(vehicle):
    def move(self):
        print("fly")
car1 = car("audi","q5")
boat1 = boat("sailer100","idk")
plane1 = plane("airways","2030")
for x in (car1,boat1,plane1):
    print(x.brand,x.model)
    x.move()

class Cat():
    def sound(self):
        print("Meow")
class Fox():
    def sound(self):
        print("Wa-pa-pa-pa-pow!")
cat1 = Cat()
f1 = Fox()
for x in (cat1,f1):
    x.sound()
