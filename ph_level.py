grade = int(input("whats your grade:"))
if grade > 90:
    print('A')
elif grade > 80:
    print('B')
elif grade > 70:
    print('C')
elif grade > 60:
    print('D')
elif grade > 50:
    print('E')
else:
    print('F')




ph = int(input("Enter a ph valeu(0-4): "))
if ph > 7:
    print('Basic')
elif ph < 7:
    print('Acidic')
else:
    print('Natural')