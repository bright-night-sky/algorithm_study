# https://www.acmicpc.net/problem/2523

# N 입력 (1 <= N <= 100)
N = int(input())

# 결과를 보면 2XN-1 번째 줄까지 있다.
# 첫 번째 줄부터 N번째 줄,
# N+1번째 줄부터 2XN-1번째 줄을 나눠서 출력한다.

# 첫 번째 줄부터 N번째 줄 출력
for i in range(0, N):
    # 별 출력
    # 1, 2, 3, ... 순으로 출력
    print('*' * (i + 1))

# N+1번째 줄부터 끝줄(2XN-1번째)까지 출력
for i in range(0, N-1):
    # 별 출력
    # 1, 2, 3, ... 을 역순으로 출력
    print('*' * (N - 1 - i))