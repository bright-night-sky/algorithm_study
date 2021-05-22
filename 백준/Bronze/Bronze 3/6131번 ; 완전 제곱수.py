# https://www.acmicpc.net/problem/6131

# readline을 사용하기 위해 import합니다.
from sys import stdin

# 첫째 줄에 N을 입력합니다.
# 1 <= ㅜ <= 1,000
N = int(stdin.readline())

# A, B 쌍의 개수를 저장할 변수를 선언합니다.
AB_pair_cnt = 0

# 1 <= B <= A <= 500
# B를 1부터 500까지 반복해봅니다.
for B in range(1, 501):
    # A를 B부터 500까지 반복해봅니다.
    for A in range(B, 501):
        # B의 제곱이 A의 제곱보다 N만큼 작다면
        if A ** 2 - B ** 2 == N:
            # A, B 쌍의 개수에 1을 더해줍니다.
            AB_pair_cnt += 1

# A, B 쌍의 개수를 출력합니다.
print(AB_pair_cnt)