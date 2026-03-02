thislist = ["orange", "banana", "banana", "cherry"]
print(thislist[1])
list2 = [1, 2, 3]
print(list2)
if "cherry" in thislist:
    print("yes cherry is in fruit list")

thislist[1]="apple"
print(thislist)
thislist.insert(2, "strawberry")
print(thislist)
thislist.remove("orange")
print(thislist)
list3 = [1, 2, 3]
list4 = ["a", "b", "c"]
list5 = list3+list4
print(list5)
for x in list4:
 list3.append(x)
 print(list3)

 list3.extend(list4)
 print(list3)

 #tuples
 thistuple = ("audi", "toyota", "toyota", "bmw")
 print(thistuple)
 print(len(thistuple))

 x = ("audi", "toyota", "toyota", "bmw")
 y = list(x)
 y[1]="mercedes"
 x = tuple(y)
 print(x)

tuple1 = ("audi", "toyota", "toyota", "bmw")
tuple2 = list(tuple1)
tuple2.append("orange")
tuple1 = tuple(tuple2)
print(tuple1)

list10 = ("cars", "trucks", "buses")
z = ("vans",)
list10 += z
print(list10)

list15 = ("cars", "trucks", "buses")
w = list(list15)
w.remove("trucks")
list15=tuple(w)
print(list15)

list16 = ("cars", "trucks", "buses")
print(list16)
del list16
print(list16)
