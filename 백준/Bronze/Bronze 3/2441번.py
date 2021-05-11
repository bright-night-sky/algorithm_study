# https://www.acmicpc.net/problem/2441

# N (1 <= N <= 100) 입력
N = int(input())

# 한 줄씩마다
for i in range(0, N):
    # 별 출력
    print(' ' * i, end='')
    # 공백 출력
    print('*' * (N - i))
