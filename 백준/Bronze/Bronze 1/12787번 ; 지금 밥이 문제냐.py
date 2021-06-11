# https://www.acmicpc.net/problem/12787

from sys import stdin

T = int(stdin.readline())

for test_case_idx in range(T):
    M, N = stdin.readline().rstrip().split(' ')
    result = ''

    if M == '1':
        numbers = N.split('.')

        for number in numbers:
            bin_number = bin(int(number))[2:]
            result += bin_number

        print(int('0b' + result, 2))
    else:
        N = bin(int(N))[2:]
        result = []

        if len(N) % 8 != 0:
            M = '0' * (len(N) % 8) + N

        for idx in range(0, len(N), 8):
            bin_number = '0b' + N[idx:idx+8]
            number = int(bin_number, 2)
            result.append(number)

        result = list(map(str, result))
        print('.'.join(result))