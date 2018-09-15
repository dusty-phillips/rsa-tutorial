import pytest
from .. import rsa  # easy as rsa


def test_guarantee_bits():
    assert rsa.guarantee_bits(0b0110, 4) == 0b1111
    assert rsa.guarantee_bits(0b1111, 4) == 0b1111
    assert rsa.guarantee_bits(0, 4) == 0b1001
    assert rsa.guarantee_bits(0b10101, 4) == 0b1101
    assert rsa.guarantee_bits(0b10010, 5) == 0b10011


def test_exact_randbits():
    for num_bits in range(1, 1024):
        assert rsa.exact_randbits(num_bits).bit_length() == num_bits


def test_gcd():
    assert rsa.gcd(1, 2) == 1
    assert rsa.gcd(2, 4) == 2
    assert rsa.gcd(18, 12) == 6
    assert rsa.gcd(18, 15) == 3
    assert rsa.gcd(28, 21) == 7
    assert rsa.gcd(0, 5) == 5
    assert rsa.gcd(-5, 5) == 5
    assert rsa.gcd(-10, 5) == 5


def test_modinv():
    with pytest.raises(ValueError):
        rsa.modinv(2, 4)
    with pytest.raises(ZeroDivisionError):
        rsa.modinv(1, 0)

    assert rsa.modinv(3, 4) == 3
    assert rsa.modinv(9, 4) == 1
    assert rsa.modinv(7, 4) == 3

    # if modulus is prime, invers is i ** m-2 % m
    for i in range(1, 12):
        assert rsa.modinv(i, 13) == pow(i, 11, 13)

    assert rsa.modinv(-5, 11) == 2


def test_rsa_round_trip():
    "generate a bunch of random keys and confirm encrypt/decrypt round trip"
    for i in range(2000):
        key = rsa.generate_key(15)
        message = rsa.exact_randbits(10)
        cipher = rsa.encrypt(key, message)
        decoded = rsa.decrypt(key, cipher)
        assert message == decoded
