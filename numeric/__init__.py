def base(I, b):
    """
    Base converter.

    Converts decimal number into base representation of 2 through 16.

    Complexity: O(n) pseudo-polynomial time where `n` is number of times integer can be
     divided by 2.
    :param int I: Decimal integer
    :param int b: Radix base
    :return str: Binary string
    """
    if not 1 < b <= 16:
        raise ValueError("Unable to convert to base {}".format(b))
    if I > 0:
        rem = I % b
        return base(I // b, b) + CHARS[rem]
    else:
        return ''


def gcd(a, b):
    """
    Returns greatest common divisor using Euclid's method.

    Complexity: O(n) where `n` is the larger number
    :param int a: First integer
    :param int b: Second integer
    :return int: GCD of two integers
    """
    while b:
        a, b = b, a % b
    return a


def ϕ(n):
    """
    Euler's totient function.

    Euler's totient function (also called Euler's phi function) counts the positive
     integers up to a given integer n that are relatively prime to n. It's the number of
     integers `k` in the range `1 ≤ k ≤ n` for which the greatest common divisor is `1`.

    Complexity: O(n^2)
    :param int n: Input integer
    :return int: Number of relatively prime numbers in sequence.
    """
    count = 0
    for k in range(1, n + 1):
        if gcd(n, k) == 1:
            count += 1
    return count


def swap(a, b):
    """
    Swaps two integers without using extra memory.

    Bitwise XOR sets the bits in the result to 1 if either, but not both, of the
     corresponding bits in the two operands is 1.

    Complexity: O(1), no extra space.
    :param int a:
    :param int b:
    :return tuple:
    """
    a ^= b
    b ^= a
    a ^= b
    return a, b


"""
Constants used in this module
"""
CHARS = "0123456789abcdef"
