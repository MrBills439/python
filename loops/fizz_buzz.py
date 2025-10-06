for i in range(10):
  print(i)

  # Fizz Buzz 🐝
# Codédex

for num in range(1, 101):
  if num % 3 == 0 and num % 5 == 0:
    print('FizzBuzz')
  elif num % 3 == 0:
    print('Fizz')
  elif num % 5 == 0:
    print('Buzz')
  else:
    print(num)

   

    i = 0

while i < 6:
  j = 0
  while j < 6:
    print(i * j)
    j = j + 1
  i = i + 1