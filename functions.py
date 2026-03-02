def my_function():
    print("this is my python function")
my_function()
my_function()

temp1 = 71
cel1 = (temp1-32)*5/9
print(cel1)

temp2 = 95
cel2 = (temp2-32)*5/9
print(cel2)

def degrees(fahrenheit):
    return(fahrenheit-32)*5/9
print(degrees(71))
print(degrees(95))

def greetings():
    return "habari yako"
print(greetings())

#arguments
def name(fname):
    print(fname+ "peter")
name("john")
name("john")

def car(brand, color):
    print(brand + " " + color)
car("bmw", "white")
car("toyota", "red")

def user(name = "peter"):
    print("hello", name)
user()

def my_nationality(country = "kenya"):
    print("i am from", country)
my_nationality()
my_nationality("japan")
my_nationality("tanzania")

def my_func(x, y):
    return x+y
result = my_func(5, 10)
print(result)

def my_fnct():
    x = 10
    print(x)
my_fnct()

y = 30
def my_fncton():
    print(y)
my_fncton()

#range (start, stop, step)
x = range(20)
print(x)
print(list(x))

y = range(3, 20)
print(list(y))

z = range(4, 20, 2)
print(list(z))

for i in range(30):
    print(i)

#arays
cars = ["bmw", "toyota", "mazda", "audi"]
print(cars)
for x in cars:
    print(x)

import my_module
my_module.greetings("john")

import my_module
a = my_module.person1["country"]
print(a)

import datetime
x = datetime.datetime.now()
print(x)

p = min(10, 20, 30, 5, 2)
q = max(40, 50, 60, 70)
print(p)
print(q)

import math
x = math.sqrt(100)
print(x)
import math
y = math.pi
print(y)

#JSON
import json
person1 = '{"name":"peter", "age":"18", "country":"kenya"}'
y = json.loads(person1)
print(y["age"])

person3 = {"name":"peter", "age":"18", "country":"kenya"}
z = json.dumps(person3)
print(z)

