'''
Attempted to make trial_division faster using cython. It got a 10x
speedup, but of course, it only works with 64 bit integers. When
working with 1024 bit or higher RSA keys, it can't handle the math.

To build this file on Linux:

    cython --annotate cy_is_prime.pyx
    gcc -shared -pthread -fPIC -fwrapv -O2 -Wall -fno-strict-aliasing \
      -I/home/dusty/.pyenv/versions/3.7.0/include/python3.7m \
      -o cy_is_prime.so \
      cy_is_prime.c

'''

#cython: boundscheck=False, wraparound=False, nonecheck=False, cdivision=True
import math
import random


def trial_division(long long py_number):
    cdef long long number = py_number
    cdef long long redundant_above = math.ceil(math.sqrt(number))
    if number <= 1:
        return 0
    if number == 2 or number == 3 or number ==5:
        return 1
    if not number % 2 or not number % 3 or not number % 5:
        return 0

    cdef long long i = 5
    while i < redundant_above +1:
        if not number % i or not number % (i + 2):
            return 0
        i += 6
    return 1
