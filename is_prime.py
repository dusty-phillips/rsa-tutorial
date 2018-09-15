import math
import random

FIRST_PRIMES = [2, 3, 5, 7, 13, 17, 19, 23]


def trial_division(number: int) -> int:
    if number <= 1:
        return False
    for prime in FIRST_PRIMES:
        if number == prime:
            return True
        if not number % prime:
            return False

    redundant_above = math.ceil(math.sqrt(number))
    for i in range(5, redundant_above + 1, 6):
        if not number % i or not number % (i + 2):
            return False
    return True


def miller_rabin(number: int) -> int:
    if number <= 1:
        return False
    for prime in FIRST_PRIMES:
        if number == prime:
            return True
        if not number % prime:
            return False

    odd_factor = number - 1
    mod_levels = 0
    while odd_factor % 2 == 0:
        odd_factor = odd_factor // 2
        mod_levels += 1

    for trials in range(40):
        witness = random.randrange(2, number - 1)
        mod_pow = pow(witness, odd_factor, number)
        if mod_pow == 1:
            continue
        for i in range(mod_levels):
            if mod_pow == (number - 1):
                break
            else:
                i = i + 1
                mod_pow = (mod_pow ** 2) % number
        else:
            return False
    return True
