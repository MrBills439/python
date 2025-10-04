guess = 0

while guess != 6:
  guess = int(input('Guess the number: '))

print("YOU GOT THIS!")


guess = 0
tries = 0

while guess != 6 and tries < 5:
  guess = int(input('Guess the number: '))
  # update tries