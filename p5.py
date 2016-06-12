'''
    Problem 5:
    2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

    What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

    https://projecteuler.net/problem=5

    Actually, this is not an optimal solution. Because the program have to run quite a long time to find the solution            
'''

divisible_range = 20
counter = 2520 # since 2520 is the smallest for 1 to 10, so use it as base
while True:
    divisible_check = True
    for number in range (1,divisible_range + 1):
        if counter %  number != 0:
            divisible_check = False
            break
    if divisible_check == True:
        break
    else:
        counter += 10 # make it divisible by 2 and 5

print(counter)
