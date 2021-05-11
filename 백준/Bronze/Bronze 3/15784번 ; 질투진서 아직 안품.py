# https://www.acmicpc.net/problem/15784

# 첫째 줄에 의자가 놓인 행과 열의 수 N,
# 진서가 앉은 의자가 위치한 행 a, 열 b를 입력합니다.
# 1 <= N <= 1000
N, a, b = map(int, input().split(' '))

# 두 번째 줄부터 N+1 줄까지 강의실에 앉아있는 학생들의 매력지수를 입력합니다.
for i in range(0, N):
    # 한 번에 한 줄씩 입력합니다.
    