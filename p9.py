#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
  Problem 10:
  The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

  Find the sum of all the primes below two million.

  https://projecteuler.net/problem=10
'''
from math import sqrt

def isPrime(numberToCheck):
  for i in range(2, int(sqrt(numberToCheck)) + 1):
    if numberToCheck % i == 0:
      return False
  return True

number = 2
sum = 0
while (number < 2000000):
  if (isPrime(number)):
    sum += number
  number += 1

print(sum)