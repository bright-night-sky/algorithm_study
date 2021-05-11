# https://www.acmicpc.net/problem/2443

# N (1 <= N <= 100) 입력
N = int(input())
# 한 줄씩마다
for i in range(0, N):
    # 공백 출력
    print(' ' * i, end='')
    # 첫째 줄에는 별 2XN-1개, 둘째 줄에는 별 2XN-3개, ..., N번째 줄에는 별 1개 찍기
    # 별 출력 : 1, 3, 5, 7, 9, ... 을 역순으로 출력 : 등차수열 2n+1
    print('*' * (2 * N - (2 * i + 1)))

