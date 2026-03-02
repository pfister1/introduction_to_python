#NUMBER1-Write a program that creates a variable called name and stores your name in it. Then print: 
#My name is ______
print("my name is")
name = input()
print(f"my name is {name}")
name = "Peter"
print("My name is"+ " "+ name)

#NUMBER2-Write a program that creates two variables a = 12 and b = 4, and prints: 
#• Their sum 
#• Their difference 
#• Their product 
#• Their division
a = 12
b = 4
c = a + b
print(c)
d = a - b
print(d)
e = a * b
print(e)
f = a / b
print(f)

#NUMBER3-Write a program that creates a variable called number and stores the value 25, then prints the 
#square of the number. 
number = 25
print(number*number)

#NUMBER4-Write a program that creates a variable x = 49, then finds and prints its square root.
import math
x = math.sqrt(49)
print(x)

#NUMBER5-Write a program that asks the user to enter a number and prints its square. 
import math
x = input("enter a number")
y = (float(x)*float(x))
print(f" square of {x} is {y}")

#NUMBER6-Write a program that asks the user to enter a number and prints its square root.
import math
x = input("enter a number")
y = math.sqrt(float(x))
print(f"squareroot of {x} is {y}")

#OR
import math
x = input("enter a number")
y = (float(x))
if y :
    print(f"the squareroot of {x} is {y}")

#NUMBER7-Write a program that asks the user to enter two numbers and prints the larger number. 
import math
x = int(input("enter the first number:"))
y = int(input("enter the second number:"))
if x > y:
    print(f"larger number is:", x)
else:
    print(f"larger number is:", y)

#NUMBER8-Write a program that asks the user to enter a number and checks whether it is even or odd. 
x = int(input("enter a number:"))
if x % 2 == 0:
    print(x, "is an even number")
else:
    print(x, "is an odd number") 

#NUMBER9-Write a program that prints all even numbers from 1 to 20.

#NUMBER10-Write a program that asks the user to enter a number n and prints all odd numbers from 1 to n.
n = int(input("enter a number:"))
for b in range(1, n+1):
    if b % 2 != 0:
        print(b)

#NUMBER11-Write a program that prints numbers from 1 to 10 using a for loop.
for x in range(1, 11):
    print(x)
#NUMBER15-Write a program that asks the user to enter a number: 
#• If the number is positive, print its square root. 
#• If the number is negative, print: "Cannot calculate square root". 
import math
i = int(input("enter a number"))
if i>=0:
    print("square root is:", math.sqrt(i))
else:
    print("cannot calculate square root")

#NUMBER16-Write a program that defines a function which takes a number as a parameter and returns its 
#square.
def parameter(b):
    return b*b
print(parameter(10))

#NUMBER17-Write a program that defines a function which checks whether a number is even or odd.
def no_checker(n):
    if n % 2 == 0:
        return "even number"
    else:
        return " odd number"
print(no_checker(6))
#NUMBER19-Write a program that: 
#1. Asks the user to enter a number 
#2. Prints whether it is even or odd 
#3. Prints its square 
#4. Prints its square root (if possible)
import math
n = int(input("enter a number:"))
# Even or Odd number
if n %2 == 0:
    print("even number")
else:
    print("odd number")
# Square
print("the square is:", n*n)
# Square root
if n >= 0:
    print("square root is:", math.sqrt(n))
else:
    print("cannot calculate square root")