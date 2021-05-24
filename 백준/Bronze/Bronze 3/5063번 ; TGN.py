# https://www.acmicpc.net/problem/5063

# readline을 사용하기 위해 import합니다.
from sys import stdin

# 첫째 줄에 테스트 케이스의 개수 N을 입력합니다.
N = int(stdin.readline())

# 테스트 케이스의 개수 N만큼 반복합니다.
for test_case_idx in range(N):
    # 광고를 하지 않았을 때 수익 r, 광고를 했을 때의 수익 e, 광고 비용 c를 공백으로 구분해 입력합니다.
    # 각각 정수형으로 변환합니다.
    # -10^6 <= r, e <= 10^6
    # 0 <= c <= 10^6
    r, e, c = map(int, stdin.readline().split(' '))
    # 광고를 했을 때의 순수익을 저장하는 변수를 선언합니다.
    advertise_net_gain = e - c

    # 광고했을 때의 순수익이 광고를 하지 않았을 때의 수익보다 크다면
    if advertise_net_gain > r:
        # advertise를 출력합니다.
        print("advertise")
    # 광고했을 때의 순수익이 광고를 하지 않았을 때의 수익과 같다면
    elif advertise_net_gain == r:
        # does not matter를 출력합니다.
        print("does not matter")
    # 광고했을 때의 순수익이 광고를 하지 않았을 때의 수익보다 작다면
    else:
        # do not advertise를 출력합니다.
        print("do not advertise")