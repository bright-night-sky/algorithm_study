# https://www.acmicpc.net/problem/14612

from sys import stdin

N, M = map(int, stdin.readline().split(' '))
orders = []

for query_idx in range(N):
    query = stdin.readline().rstrip().split(' ')

    if query[0] == 'order':
        order = list(map(int, [query[1], query[2]]))
    elif query[0] == 'sort':
        orders.sort(key=lambda order: order[1])
    elif query[0] == 'complete':
        complete_table_idx = orders.index()