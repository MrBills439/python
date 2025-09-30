grade = int(input("What is your grade? "))

if grade >= 60:
    print("You passed")
else:
    print("You failed")


# grade.py 
# i did this code to handle a decimal number in other for anyone who as decimal number.
try:
    grade = float(input("What is your grade? "))
    if grade > 60:
        print("You passed")
    else:
        print("You failed")
except ValueError:
    print("Please enter a valid number.")
