#!/usr/bin/env python3

import sys


PRIMES = {
    0: False,
    1: False,
    2: True,
    3: True,
}


def is_prime(number):
    if number in PRIMES:
        return PRIMES[number]

    if number % 2 == 0:
        PRIMES[number] = False
        return False

    for i in range(3, int(number ** 0.5) + 1, 2):
        if number % i == 0:
            PRIMES[number] = False
            return False

    PRIMES[number] = True
    return True


def log_progress(i, total):
    if i == 0:
        print("Progress: {0:.2f} %".format(0.0), end='')
    elif i == total:
        print("\rProgress: Complete!")
    else:
        percentile = total / 10000
        if i % percentile == 0:
            progress = i / total * 100
            print("\rProgress: {0:.2f} %".format(progress), end='')


def sums_of_primes(limit):
    sums = []
    current_sum = 0
    current_primes = []

    for i in range(limit):
        log_progress(i, limit)

        if not is_prime(i):
            continue

        # pre-empt walk backwards, and taking the data
        while current_sum + i > limit:
            current_sum -= current_primes.pop(0)
            if not current_sum:
                break
            sums.append((current_sum, current_primes[:]))

        current_sum += i
        current_primes.append(i)
        sums.append((current_sum, current_primes[:]))

    print("\rProgress: Complete!")

    return sums


def run(limit):
    sums = sums_of_primes(limit)

    longest_prime = []
    for key, value in sums:
        if key > limit:
            continue
        if not is_prime(key):
            continue

        if len(value) > len(longest_prime):
            longest_prime = sorted(value)

    print("Under limit: {}".format(limit))
    print("Longest sum of primes: {}".format(sum(longest_prime)))
    print("prime numbers count: {}".format(len(longest_prime)))
    print("prime numbers:")
    print(longest_prime)


def main():
    limit = 1000000
    run(limit)


if __name__ == '__main__':
    main()
