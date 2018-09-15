 *  generate two large random primes. well how does one do that?
 *  primes cannot be calculated, they can only be confirmed
 *  so generate two random numbers and check if they are prime
 *  how to check if prime?
     *  [There are several algorithms](https://en.wikipedia.org/wiki/Primality_test)
     *  Tested my implementation by copying https://primes.utm.edu/lists/small/10000.txt into a python set and comparing to mine

I tried this but too slow:

    def is_prime(number):
        if number <= 1:
            return False
        for prime in FIRST_PRIMES:
            if number == prime:
                return True
            if not number % prime:
                return False

        redundant_above = math.ceil(math.sqrt(number))
        for i in range(FIRST_PRIMES[-1], redundant_above + 1, 6):
            if not number % i or not number % (i + 2):
                return False
        return True

dicked around with cython a bit, but fuggit, I just pip installed sympy


 *  The secrets module is cryptographically secure https://docs.python.org/3/library/secrets.html
 *  since RSA is usually quoted in "x-bit encryption", try to generate an appropriate number of bits. each of the two numbers should have about half the number of bits
 *  use namedtuple so it can't be changed

 *  What the hell is a totient? Oh... it's just (p-1)*(q-1) why didn't you say so?

 *  algorithm says "select e" such that. Some say it can be hardcoded to 65537 (2**16)
 *  can use math.gcd, but implemented the euclidean algorithm for better understanding
     *  The iterative version is hard to understand but honestly it's just
     *  see https://brilliant.org/wiki/extended-euclidean-algorithm/
 *  totient should/could use carmeichl instead of euler totient
 *  Algorithm for modinv seems convoluted, but it's just "We observed that a number x had an inverse mod 26 (i.e., a number y so that xy = 1 mod 26) if and only if gcd(x, 26) = 1." http://www-math.ucdenver.edu/~wcherowi/courses/m5410/exeucalg.html
