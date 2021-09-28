"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we
get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""


def is_multiple(num, divisors):
    for divisor in divisors:
        if num % divisor == 0:
            return True
    return False


def sum_multiples(N, divisors):
    total = 0

    for i in range(N):
        if is_multiple(i, divisors):
            total += i

    return total


if __name__ == '__main__':
    print(sum_multiples(1000, (3, 5)))
