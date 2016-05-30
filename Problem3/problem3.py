'''
    Problem 3:
    The prime factors of 13195 are 5, 7, 13 and 29.

    What is the largest prime factor of the number 600851475143 ?

    https://projecteuler.net/problem=3
'''

number = 600851475143
largest_prime_factor = 1
counter = 2

while number > 1:
    if (number % counter == 0):
        number /= counter
        if (largest_prime_factor < counter):
            largest_prime_factor = counter
        counter = 2
    else:
        counter += 1

print largest_prime_factor
