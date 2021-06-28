# https://www.acmicpc.net/problem/3944

from sys import stdin


def convertDecimal(num, numeral):
    num_len = len(num)
    result = 0

    for idx in range(num_len):
        result += int(num[idx]) * (numeral ** (num_len - idx - 1))

    return result


T = int(stdin.readline())

for test_case_idx in range(T):
    B, D = stdin.readline().rstrip().split(' ')
    B = int(B)
    decimal_num = convertDecimal(D, B)

    print(decimal_num % (B - 1))