# https://www.acmicpc.net/problem/15700

# N, M 입력
# 1 <= N, M <= 1,000,000,000
N, M = map(int, input().split(' '))

# N X M 벽에 2X1, 1X2 크기의 타일을 최대로 채우는 갯수는
# NXM을 2로 나눈 몫이다.
print(N * M // 2)