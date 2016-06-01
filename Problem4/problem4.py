'''
    Problem 4:
    A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

    Find the largest palindrome made from the product of two 3-digit numbers.

    https://projecteuler.net/problem=4
'''

first_number = 999
second_number = 999
array_of_result = []


def palindrome(int):
    return str(int) == str(int)[::-1]

for first_counter in range(first_number,100,-1):
    for second_counter in range(second_number, 100, -1):
        prod = first_counter * second_counter
        if (palindrome(prod)):
            array_of_result.append(prod)

print(max(array_of_result))
