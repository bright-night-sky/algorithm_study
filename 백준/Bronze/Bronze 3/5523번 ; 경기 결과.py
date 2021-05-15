# https://www.acmicpc.net/problem/5523

# readline을 사용하기 위해 import합니다.
from sys import stdin

# 첫째 줄에는 라운드의 수인 정수 N을 입력합니다.
# 1 <= N <= 1,000,000
N = int(stdin.readline())

# A가 이긴 횟수를 저장할 변수를 선언합니다.
A_win_cnt = 0
# B가 이긴 횟수를 저장할 변수를 선언합니다.
B_win_cnt = 0

# 라운드의 수 N만큼 반복해봅니다.
for round_idx in range(N):
    # A, B의 점수인 정수 Ai, Bi를 공백으로 구분해 입력합니다.
    # 0 <= Ai, Bi <= 100
    Ai, Bi = map(int, stdin.readline().split(' '))

    # A의 점수가 B의 점수보다 크다면
    if Ai > Bi:
        # A가 이긴 횟수에 1을 더해줍니다.
        A_win_cnt += 1
    # A의 점수가 B의 점수보다 작다면
    elif Ai < Bi:
        # B가 이긴 횟수에 1을 더해줍니다.
        B_win_cnt += 1

# A가 이긴 횟수와 B가 이긴 횟수를 차례대로 출력합니다.
print(A_win_cnt, B_win_cnt)