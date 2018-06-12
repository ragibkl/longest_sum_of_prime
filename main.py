#!/usr/bin/env python3

import sys

NOT_PRIMES = [ 0, 1 ]
PRIMES = [ 2, 3 ]

def is_prime(number):
    if number in NOT_PRIMES:
        return False

    if number in PRIMES:
        return True

    for i in range(2, number):
        if number % i == 0:
            NOT_PRIMES.append(number)
            return False

    PRIMES.append(number)
    return True


def sums_of_primes(limit):
    prime_list = [ i for i in range(limit) if is_prime(i) ]
    prime_list = reversed(prime_list)

    sums = []
    current_sum = 0
    current_primes = []
    for prime in prime_list:
        current_sum += prime
        current_primes.append(prime)

        while current_sum > limit:
            current_sum -= current_primes.pop(0)

        sums.append((current_sum, current_primes[:]))

    return sums


def main():
    limit = 1000
    sums = sums_of_primes(limit)

    longest_sum = 0
    longest_prime = []
    for key, value in sums:
        if key > limit:
            continue
        if not is_prime(key):
            continue

        if len(value) > len(longest_prime):
            longest_sum = key
            longest_prime = sorted(value)

    print("Under limit: {}".format(limit))
    print("Longest sum of primes: {}".format(longest_sum))
    print("with primes: {}, with {} terms".format(longest_prime, len(longest_prime)))


if __name__ == '__main__':
    main()
