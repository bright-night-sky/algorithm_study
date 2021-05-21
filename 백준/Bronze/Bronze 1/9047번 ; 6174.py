# https://www.acmicpc.net/problem/9047

from sys import stdin

T = int(stdin.readline())

for test_case_idx in range(T):
    number = stdin.readline().rstrip()

    phase = 0
    while True:
        if number == '6174':
            print(phase)
            break

        min_number = int(''.join(sorted(number)))
        max_number = int(''.join(sorted(number, reverse=True)))
        phase_result = max_number - min_number
        number = str(phase_result)
        phase += 1