# import sys
#
#
# def is_prime(n):
#     for p in primes:
#         if n % p == 0:
#             return
#     else:
#         primes.append(n)
#
#
# def Goldbach(n):
#     front, rear = 0, prime_length
#     while front <= rear:
#         if primes[front] + primes[rear] > n:
#             rear -= 1
#         elif primes[front] + primes[rear] < n:
#             front += 1
#         else:
#             print(f'{n} = {primes[front]} + {primes[rear]}')
#             return
#
#     print('Goldbach\'s conjecture is wrong.')
#
#
# input = sys.stdin.readline
# START = 29
# evens = []
# maxi = 0
# while True:
#     even = int(input())
#     if even == 0:
#         break
#     maxi = max(maxi, even)
#     evens.append(even)
#
# primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
# length_cnt = len(primes)
# cnts = [0] * length_cnt
# for i in range(1, length_cnt):
#     cnts[i] = START % primes[i]
#
# for num in range(START + 2, maxi, 2):
#     for i in range(1, length_cnt):
#         cnts[i] += 2
#         cnts[i] %= primes[i]
#
#     if 0 in primes:
#         continue
#
#     is_prime(num)
#
# prime_length = len(primes) - 1
# for even in evens:
#     Goldbach(even)
import sys


def Goldbach(n):
    front, rear = 0, primes_length - 1
    while front <= rear:
        if primes[front] + primes[rear] > n:
            rear -= 1
        elif primes[front] + primes[rear] < n:
            front += 1
        else:
            print(f'{n} = {primes[front]} + {primes[rear]}')
            return

    print('Goldbach\'s conjecture is wrong.')


input = sys.stdin.readline
evens = []
maxi = 0
while True:
    even = int(input())
    if even == 0:
        break
    maxi = max(maxi, even)
    evens.append(even)

is_primes = [False, False, True] + [True, False] * (maxi // 2 - 1)
primes = [2]
for i in range(3, maxi, 2):
    if not is_primes[i]:
        continue
    for m in range(2 * i, maxi, i):
        is_primes[m] = False
    primes.append(i)

primes_length = len(primes)
for even in evens:
    Goldbach(even)
