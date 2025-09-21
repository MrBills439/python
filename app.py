import math
course = "python Programming"
print(course.upper())
print(course)
print(course.strip())
print(course.replace("p", "j"))
print("pro" in course)
print("Pro" in course)


#working with numbers 
print(10 + 3)
print(10 - 3)


print(round(2.9))
print (abs(-2.9))

print(math.ceil(2.2))



# trying
fruit = "Apple"
print(fruit[1:-1])

print(bool("false"))

# compariosn Operations 
tempreature = 35
if tempreature > 30:
    print("It's warm")
    print("Drink water")
print("Done")

tempreature = 25
if tempreature > 30:
    print("It's warm")
    print("Drink water")

elif tempreature > 20:
    print("it's Nice")
else:
    print("it's cold")
print("Done")


#Ternary Operator
age = 22
if age >= 22:
    print("Eligible")
else:
    print("Not eligible")

# Another way to make the code nice and clean
age = 18
if age >= 20:
    message = "Eligible"
else:
    message = "Not Eligible"
print(message)

# Another way to make the code nice and clean
message = "Eligible" if age >= 12 else "Not Eligible"
print(message)

# logical Operator
high_income = False
good_credit = True

if high_income or good_credit:
    print("Eligble")
else:
    print("Not Eligble")



high_income = False
good_credit = True
student = True

if not student:
    print("Eligble")
else:
    print("Not Eligble")

high_income = False
good_credit = True
student =True

if high_income or good_credit or not student:
    print("Eligble")
else:
    print("Not Eligble")


#chaning Comparison Operators

# age should be between 18 and 65
age = 22

if 18 <= age < 65:
    print("Eligible")

if 10 == "10":
    print("a")
elif "bag" > "apple" and "bag" > "cat":
    print("b")
else:
    print("C")

#For loops
for number in range(4, 10, 7):
    print("Welcome", number, number * ".")

#for...Else
successful = True
for numbner in range(3):
    print("Attempt")
    if successful:
        print("Successful")
        break

successful = False
for numbner in range(3):
    print("Attempt")
    if successful:
        print("Successful")
        break
else:
    print("Attempted 3 times and failed")

#Nested loops
for x in range(5):
    for y in range(3):
        print(f"({x}, {y})")

#Interables
print(type(5))
print(type(range(5)))

for x in "Python":
    print(x)
for x in [1, 2, 3, 4]:
    print(x)



count = 0
for number in range(1,10):
    if number % 2 == 0:
        count += 1
        print(number)
print(f"we have {count} even numbers")


# functions 
#def greet(first_name, last_name):
#    print("Welcome aboard")
#   print("Have fun")
#
#greet("feddy", "BIlls")


def greet(name):
    print(f"Hi {name}")

def get_greeting(name):
    return f"Hi {name} and i am leaning to better my pyhton skills"

message = get_greeting("Feddy")
file = open("content.txt", "w")
file.write(message)


# Keyword Agrugumnets
def increment(number, by=1):
    return number + by

print(increment(2, 5))


#Arags,wait,what
def multiply(*numbers):
    print(numbers)
#
#multiply(2, 3, 4, 5)

def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


print(multiply(2, 3, 4, 5)) 