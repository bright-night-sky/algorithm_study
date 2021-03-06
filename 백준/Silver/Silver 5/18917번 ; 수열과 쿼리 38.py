# https://www.acmicpc.net/problem/18917

from sys import stdin
from collections import deque

A = deque([0])
M = int(stdin.readline())

for query_idx in range(M):
    query = stdin.readline().rstrip()

    if query[0] == '1':
        x = int(query.split(' ')[1])
        A.append(x)
    elif query[0] == '2':
        x = int(query.split(' ')[1])
        A.remove(x)
    elif query[0] == '3':
        print(sum(A))
    elif query[0] == '4':
        xor_result = A[0]

        for idx in range(1, len(A)):
            xor_result = A[idx] ^ xor_result

        print(xor_result)