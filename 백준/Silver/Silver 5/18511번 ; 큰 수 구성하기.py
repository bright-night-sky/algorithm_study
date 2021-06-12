# https://www.acmicpc.net/problem/18511

from sys import stdin


N, K = stdin.readline().split(' ')
K = int(K)
elements = sorted(list(map(int, stdin.readline().split(' '))), reverse=True)
max_element = max(elements)
N_front = int(N[0])
result = ''

for element in elements:
    if element <= N_front:
        result += str(element)
        break

