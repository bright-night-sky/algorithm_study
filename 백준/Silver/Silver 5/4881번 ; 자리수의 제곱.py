# https://www.acmicpc.net/problem/4881

from sys import stdin

while True:
    A, B = stdin.readline().rstrip().split(' ')

    if A == B == '0':
        break

    A_sequence = [int(A)]
    B_sequence = [int(B)]

    while True:
        number = 0

        for position in str(A):
            number += int(position)

            if A_sequence.count(number) == 1:
                same_number_idx = A_sequence.index(number)
                A_sequence = A_sequence[same_number_idx:]
                break
            else:
                A_sequence.append(number)
                A = number

    while True:
        number = 0

        for position in str(B):
            number += int(position)

            if B_sequence.count(number) == 1:
                same_number_idx = B_sequence.index(number)
                B_sequence = B_sequence[same_number_idx:]
                break
            else:
                B_sequence.append(number)
                B = number

    print(A_sequence, B_sequence)