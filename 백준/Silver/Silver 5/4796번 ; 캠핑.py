# https://www.acmicpc.net/problem/4796

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 테스트 케이스의 번호를 저장하는 변수를 선언합니다.
# 1부터 시작하므로 1로 초기화합니다.
case = 1

# L, P, V가 모두 0일 때까지 반복합니다.
while True:
    # 캠핑장을 연속하는 P일 중, L일 동안만 사용할 수 있다. 강산이는 이제 막 V일짜리 휴가를 사직했다.의
    # L, P, V를 공백으로 구분해 입력합니다.
    # 1 < L < P < V
    # 각각 정수형으로 변환합니다.
    L, P, V = map(int, stdin.readline().split(' '))

    # L, P, V가 모두 0이라면
    if L == P == V == 0:
        # 반복문을 탈출합니다.
        break

    # 휴가 일수 V를 연속하는 P일로 나눈 몫을 저장하는 변수를 선언합니다.
    P_cnt = V // P
    # 휴가 일수 V를 연속하는 P일로 나눈 뒤의 나머지를 저장하는 변수를 선언합니다.
    remain_day = V % P
    # 캠핑장을 최대로 사용할 수 있는 일수를 저장하는 변수를 선언합니다.
    # P_cnt와 L의 곱으로 초기화합니다.
    camping_day = P_cnt * L

    # remain_day가 L보다 크거나 같다면
    if remain_day >= L:
        # remain_day동안 캠핑장을 사용할 수 있는 L일 모두 캠핑장을 사용할 수 있으므로
        # camping_day에 L을 더해줍니다.
        camping_day += L
    # remain_day가 L보다 작다면
    else:
        # remain_day만큼 더 캠핑장을 사용할 수 있으므로
        # camping_day에 remain_day를 더해줍니다.
        camping_day += remain_day

    # 출력 형식에 맞게 출력합니다.
    print(f'Case {case}: {camping_day}')

    # 테스트 케이스의 번호에 1을 더해줍니다.
    case += 1