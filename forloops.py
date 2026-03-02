fruits = ["orange", "apple", "pears"]
for x in fruits:
    print(x)

for x in "banana":
    print(x)

fruits = ["orange", "apple", "pears"]
for x in fruits:
    if x == "apple":
        continue
    print(x)

for x in range(10):
    print(x)
else:
    print("finally done")

color = ["white", "blue", "red"]
fruits = ["orange", "apple", "pears"]
for x in color:
    for y in fruits:
        print(x, y)

