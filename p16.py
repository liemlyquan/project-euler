'''
  Problem 16:
  215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

  What is the sum of the digits of the number 21000?

  https://projecteuler.net/problem=5
'''

number = str(2**1000)
print("Number", number)


sum = 0
while (len(number) > 1):
  sum += int(number[len(number) - 1])

  number = number[:-1]
  print(number)
  print(sum)

print(sum)
