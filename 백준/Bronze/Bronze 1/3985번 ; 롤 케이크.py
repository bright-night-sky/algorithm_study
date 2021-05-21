# https://www.acmicpc.net/problem/3985

from sys import stdin

L = int(stdin.readline())
N = int(stdin.readline())
expected_long_piece = 0
expected_long_piece_person = None

for audience_idx in range(N):
    Pi, Ki = map(int, stdin.readline().split(' '))
    expected_piece = Ki - Pi + 1

    if expected_piece > expected_long_piece:
        expected_long_piece = expected_piece
        expected_long_piece_person = audience_idx + 1

    