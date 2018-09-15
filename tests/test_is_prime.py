import pytest
from ..is_prime import trial_division, miller_rabin
from .primes import primes, max_in_set, large_prime


def test_trial_division():
    my_primes = {p for p in range(2, max_in_set + 1) if trial_division(p)}
    assert my_primes == primes

    # too slow
    # result = trial_division(large_prime)


def test_miller_rabin():
    my_primes = {p for p in range(2, max_in_set + 1) if miller_rabin(p)}
    assert my_primes == primes
    assert miller_rabin(large_prime)


@pytest.mark.skip
def test_against_known_implementation():
    import sympy
    import secrets

    for i in range(2000):
        to_test = secrets.randbits(1024)
        assert sympy.isprime(to_test) == miller_rabin(to_test)
