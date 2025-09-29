#WELCOME NOTES
#name = input("what is your name ?...")
#age = input("what is your age ?...")
#purpose = input("what is your purpose for this comming?...")
#
#print("\n---------")
#print(f"Wellcome to the family, {name}")
#print(f"You are, {age} old ")
#print(f"My purpose here is {purpose}")

 


pizza = 2.99
coke = 0.99

total = pizza + coke

tip = total * 0.3
print(tip)

#
#Create a temperature.py program that converts a number from Fahrenheit (°F) to Celsius (°C).
#
#Google the current temperature of Brooklyn, NY (where Codédex is based) in °F.
#
#Use the following formula and write it out in Python:
#
#
#Celsius= 
#1.8
#(Fahrenheit−32)

temp_f = 56
temp_c = (temp_f - 32) / 1.8

print(temp_c)

score = 2 ** 2
score = 2 ** 3 
score = 2 ** 4

print(score)

weight = 92.3
height = 1.86

bmi = weight / (height**2)

print(bmi)



username = input('Enter your name: ')
print(f"Your name is {username}")

username = input('Enter your name: ')

print(username)


age = int(input('what is your age? '))

print(age)


#a = int(input('Enter a: '))
#b = int(input('Enter b: '))
#
#c = (a**1 + b**2) ** 0.5
#print(c)



a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

root1 = (-b + (b*b - 4*a*c)**0.5) / (2*a)
root2 = (-b - (b*b - 4*a*c)**0.5) / (2*a)

print(root1)
print(root2)