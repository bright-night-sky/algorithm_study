# https://www.acmicpc.net/problem/3003

correct_piece = [1, 1, 2, 2, 2, 8]
current_piece = list(map(int, input().split(' ')))

for idx in range(0, len(correct_piece)):
    print(correct_piece[idx] - current_piece[idx], end=' ')