# https://www.acmicpc.net/problem/5046

# 첫째 줄에 참가자의 수 N, 예산 B, 호텔의 수 H, 고를 수 있는 주의 개수 W 입력
# 1 <= N <= 200
# 1 <= B <= 500000
# 1 <= H <= 18
# 1 <= W <= 13
N, B, H, W = map(int, input().split(' '))

# 최소 비용을 저장하는 변수
min_budget = 0

# 호텔의 수 H만큼 호텔의 정보를 입력한다.
for hotel in range(0, H):
    # 호텔의 정보를 두 줄로 입력
    # 첫 번째 줄에는 그 호텔의 일인당 숙박비용 p 입력
    # 1 <= p <= 10000
    p = int(input())
    # 두 번째 줄에는 i번째 주에 투숙 가능한 인원 a 입력
    a_list = list(map(int, input().split(' ')))