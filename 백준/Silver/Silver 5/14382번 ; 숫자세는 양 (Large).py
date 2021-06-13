# https://www.acmicpc.net/problem/14382

from sys import stdin


T = int(stdin.readline())

for test_case_idx in range(T):
    N = int(stdin.readline())
    numbers = [False] * 10
    new_N = N

    if N == 0:
        new_N = 'INSOMNIA'
    else:
        multiple = 1
        new_N = N * multiple

        while True:
            if numbers == [True] * 10:
                break

            for number in str(new_N):
                numbers[int(number)] = True

            multiple += 1

    print(f'Case #{test_case_idx+1}: {new_N}')