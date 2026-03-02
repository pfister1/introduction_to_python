# a == b equals
# a != b not equals
# a < b
# a > b
# a >= b
# a <= b

a = 23
b = 340
if b>a:
    print("b is greater than a")

number = 45
if number>=0:
    print("positive")

age = 21
if age>=18:
    print("im an adult")
    print("legal")
    print("able to vote")

user_logged_in = True
if user_logged_in:
    print("welcome back user")

a = 33
b = 23
if b>a:
    print("b is greater than a")
elif a>b:
    print("a is greater than b")

a = 50
b = 50
if b>a:
    print("b is greater than a")
if a==b:
    print("a equals to b")

score = 25
if score >=90:
    print("grade: A")
elif score>=80:
    print("grade: B")
elif score>=60:
    print("grade: C")
elif score>=45:
    print("grade: D")

a = 200
b = 33
if b>a:
    print("b is greater than a")
elif a==b:
    print("a and b equal")
else:
    print("a is greater than b")

x = 100
y = 40
if y>x:
    print("y is greater than x")
else:
    print("x is greater than y")

c = 8
if c % 2==0:
    print("the number is even")
else:
    print("the number is odd")

temparature = 2
if temparature>33:
    print("its hot outside")
elif temparature>20:
    print("its warm outside")
elif temparature>10:
    print("its cool outside")
else:
    print("its cold outside")

username = "Peter"
if len(username)>10:
    print(f"welcome,{username}!")
else:
    print("error, enter your full name")

q = 10
r =200
print("Q") if q>r else print(r)

var1 = 15
var2 = 20
max_value = var1 if var1>var2 else var2
print("max_value is:",max_value)

#and 
#or 
#not

var3 = 100
var4 = 35
var5 = 600
if var3>var4 and var5>var3:
    print("both conditions are true")
if var3>var4 or var3>var5:
    print("one condition is true")
if not var3>var4:
    print("var3 is not greater than var4")

year = 25
is_student = False
has_discount_code = True
if (year<18 or year>65) and not is_student or has_discount_code:
    print("discount applies")

date = 41
if date>10:
    print("above ten")
if date>20:
    print("above twenty")
else:
    print("not above twenty")

age1 = 25
has_license = True
if age1>=18:
    if has_license:
        print("you can drive")
    else:
        print("you need a license")
else:
    print("you cant drive")

num1 = 20
num2 = 10
if num1>num2:
    pass

#match statement
#match expression:
    #case x:
        #code block
    #case y:
        #code block

day = 7
match day:
    case 1:
        print("saturday")
    case 2:
        print("sunday")
    case 3:
        print("monday")
    case 4:
        print("tuesday")
    case _:
        print("looking forward to the weekend")

day = 6
match day:
    case 1 | 2 | 3 | 4 | 5:
        print("today is a weekday")
    case 6 | 7:
        print("is a weekend")

day = 4
month = 5
match day:
    case 1 | 2 | 3 | 4 | 5 if month == 4:
        print("today is a weekday in april")
    case 1 | 2 | 3 | 4 | 5 if month == 5:
        print("today is a weekday in may")
    case _:
        print("no exact match")

day1 = 4
month1 = 5
if month == 4 and day<=5:
    print("weekday in april")
elif month == 5 and day<=5:
    print("weekday in may")
else:
    print("no exact match")