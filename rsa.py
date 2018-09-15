import typing
from dataclasses import dataclass
from secrets import randbits

from .is_prime import miller_rabin as is_prime


@dataclass
class RSAKey:
    modulus: int
    pub_exponent: int
    priv_exponent: int


def guarantee_bits(value: int, num_bits: int) -> int:
    """
    Guarantees top and bottom bit are set 1.
    set top bit so that it is exactly the right number of bits
    bottom bit since all primes are odd, so may as well ignore them
    from the start
    """
    return value & (1 << num_bits) - 1 | (1 | 1 << (num_bits - 1))


def exact_randbits(num_bits: int) -> int:
    return guarantee_bits(randbits(num_bits), num_bits)


def random_prime(num_bits: int) -> int:
    number = exact_randbits(num_bits)
    while not is_prime(number):
        number = exact_randbits(num_bits)
    return number


def _xgcd(b: int, a: int) -> typing.Tuple[int, int]:
    "returns (gcd, multiple of modinv)"
    x0, x1 = 1, 0
    while a != 0:
        x0, x1 = x1, x0 - b // a * x1
        b, a = a, b % a
    return b, x0


def gcd(b: int, a: int) -> int:
    return _xgcd(b, a)[0]


def modinv(base: int, modulus: int) -> int:
    gcd, x = _xgcd(base, modulus)
    if gcd != 1:
        raise ValueError(f"No modular inverse for {base} {modulus}")
    return x % modulus


def generate_key(num_bits: int) -> RSAKey:
    prime1 = random_prime(num_bits // 2)
    prime2 = random_prime(num_bits // 2)
    while prime2 == prime1:
        prime2 = random_prime(num_bits // 2)
    key_modulus = prime1 * prime2
    totient = (prime1 - 1) * (prime2 - 1)
    pub_exponent = random_prime(num_bits - 2)
    while pub_exponent >= totient or gcd(pub_exponent, totient) != 1:
        pub_exponent = random_prime(num_bits - 2)
    priv_exponent = modinv(pub_exponent, totient)
    return RSAKey(key_modulus, pub_exponent, priv_exponent)  # noqa: T484


def encrypt(key: RSAKey, message: int) -> int:
    return pow(message, key.pub_exponent, key.modulus)


def decrypt(key: RSAKey, ciphertext: int) -> int:
    return pow(ciphertext, key.priv_exponent, key.modulus)
