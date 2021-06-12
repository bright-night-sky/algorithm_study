# https://www.acmicpc.net/problem/16130

from sys import stdin

N = int(stdin.readline())

for student_idx in range(N):
    demerit_info = stdin.readline().rstrip()
    demerit_point = 0

    for char in demerit_info:
        if ord('A') <= ord(char) <= ord('Z'):
            demerit_point += (ord(char) - 55)
        else:
            demerit_point += int(char)

    demerit_quotient = demerit_point // 10

    if demerit_quotient == 1:
        print(1)
    elif demerit_quotient == 2:
        print(2)
    elif demerit_quotient == 3:
        print(3)
    elif demerit_quotient == 4:
        print()