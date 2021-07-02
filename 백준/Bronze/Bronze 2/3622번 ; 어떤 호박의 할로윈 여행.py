# https://www.acmicpc.net/problem/3622

from sys import stdin


A, a, B, b, P = map(int, stdin.readline().split(' '))
two_ring = "Yes"

if P < B or P < A or A == B:
    two_ring = "No"
elif P >= B and A < B:
    if A > b:
        two_ring = "No"
elif P >= A and A > B:
    if a < B:
        two_ring = "No"

print(two_ring)