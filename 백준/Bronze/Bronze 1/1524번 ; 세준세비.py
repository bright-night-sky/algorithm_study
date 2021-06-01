# https://www.acmicpc.net/problem/1524

from sys import stdin

T = int(stdin.readline())
_ = stdin.readline()

for test_case_idx in range(T):
    N, M = map(int, stdin.readline().rstrip().split(' '))
    sejun = sorted(list(map(int, stdin.readline().rstrip().split(' '))))
    sebi = sorted(list(map(int, stdin.readline().rstrip().split(' '))))

    while True:
        if len(sejun) == 0 or len(sebi) == 0:
            break

        if sejun[0] == sebi[0]:
            sebi.pop(0)
        elif sejun[0] < sebi[0]:
            sejun.pop(0)
        elif sejun[0] > sebi[0]:
            sebi.pop(0)

    if len(sejun) == len(sebi) == 1:
        print('C')
    elif len(sejun) >= 1:
        print('B')
    elif len(sebi) >= 1:
        print('S')

    _ = stdin.readline()