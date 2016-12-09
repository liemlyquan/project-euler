#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
  Problem 7:
  By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

  What is the 10 001st prime number?

  https://projecteuler.net/problem=7
'''
from math import sqrt

def isPrime(number):
  for i in range(2, int(sqrt(number)) + 1):
    if number % i == 0:
      return False
  return True

number = 2
primeCounter = 0
while (primeCounter < 10001):
  if (isPrime(number)):
    primeCounter += 1
    print("Counter", primeCounter)
    print("Number", number)
  number += 1
