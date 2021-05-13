# https://www.acmicpc.net/problem/4134

from sys import stdin

def is_prime(num):
    half_num = num // 2

    for small_num in range(2, half_num + 1):
        if num % small_num == 0:
            return False

    return True

test_case_count = int(stdin.readline())

for test_case_idx in range(test_case_count):
    n = int(stdin.readline())

    while True:
        if is_prime(n):
            print(n)
            break

        n += 1