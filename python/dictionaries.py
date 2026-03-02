thisdict = {
    "brand": "ford",
    "model": "mustang",
    "year": "1994",
    "year": "1999"
}
print(thisdict)
x = thisdict["model"]
print(x)
x = thisdict.values()
print(x)
thisdict["year"]=1994
print(x)
x = thisdict.items()
print(x)
thisdict["color"]="red"
print(x)
thisdict["year"]=1964
print(thisdict)

thatdict = {
    "brand": "ford",
    "model": "mustang",
    "year": "1994",
    "year": "1999"
}
thatdict["color"]="black"
print(thatdict)
thatdict.update({"weight": 1800})
print(thatdict)

thatdict.pop("year")
print(thatdict)

del thatdict["model"]
print(thatdict)

thatdict.clear()
print(thatdict)

cars = {
    "car1":{
        "brand":"bmw",
        "year":2007
    },
    "car2":{
        "brand":"audi",
        "year":2008
    },
    "car3":{
        "brand":"toyota",
        "year":2023
    }
}
print(cars)
print(cars["car2"]["brand"])


car1={
        "brand":"bmw",
        "year":2007
    },
car2={
        "brand":"audi",
        "year":2008
    },
car3={
        "brand":"toyota",
        "year":2023
    }
car = {
    "car1" : car1,
    "car2" : car2,
    "car3" : car3
}
print(car)

