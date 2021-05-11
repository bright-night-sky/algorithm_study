# https://www.acmicpc.net/problem/2442

# N (1 <= N <= 100) 입력
N = int(input())

# 한 줄씩마다
for i in range(0, N):
    # 공백 출력
    print(' ' * (N - 1 - i), end='')
    # 별 출력 : 1, 3, 5, 7, 9, ... 출력 : 등차수열 2n+1
    print('*' * (2 * i + 1))