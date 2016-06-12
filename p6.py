#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    Problem 6:
    The sum of the squares of the first ten natural numbers is,

    12 + 22 + ... + 102 = 385
    The square of the sum of the first ten natural numbers is,

    (1 + 2 + ... + 10)2 = 552 = 3025
    Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

    Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

    https://projecteuler.net/problem=6
'''

first_sum = second_sum = 0
max = 100
for counter in range(1, max+1):
  first_sum += counter**2
  second_sum += counter
second_sum = second_sum ** 2
print(second_sum - first_sum)
