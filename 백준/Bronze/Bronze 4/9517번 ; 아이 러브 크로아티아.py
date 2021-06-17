# https://www.acmicpc.net/problem/9517

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 첫째 줄에 게임이 시작했을 때 폭탄을 들고 있는 사람의 번호 K를 입력합니다.
# 1 <= K <= 8
# 정수형으로 변환합니다.
K = int(stdin.readline())
# 둘째 줄에는 질문의 개수 N을 입력합니다.
# 1 <= N <= 100
# 정수형으로 변환합니다.
N = int(stdin.readline())
# 폭탄이 터지는 시간 3분 30초의 초 단위 변환한 것인 210초를 저장하는 변수를 선언합니다.
bomb_time = 210
# i번째 질문을 대답하기까지 걸린 시간들을 저장하는 변수를 선언합니다.
accum_time = 0

# 질문의 개수 N만큼 반복합니다.
for i in range(N):
    # i번째 질문을 대답하기까지 걸린 시간 T, 그 플레이어의 대답 Z를 공백으로 구분해 입력합니다.
    # 1 <= T <= 100
    # Z는 T, N, P 중 하나입니다.
    T, Z = stdin.readline().rstrip().split(' ')
    # T는 정수형으로 변환합니다.
    T = int(T)

    # accum_time에 이번 질문을 대답하기까지 걸린 시간을 더해줍니다.
    accum_time += T

    # accum_time이 폭탄이 터지는 시간보다 크거나 같다면
    if bomb_time <= accum_time:
        # 폭탄이 터지므로 사람의 번호를 출력합니다.
        print(K)
        # 폭탄이 터졌으므로 반복문을 탈출합니다.
        break

    # 질문에 대한 대답이 T인 경우
    if Z == 'T':
        # 대답이 맞았으므로 다음 사람의 번호로 넘어갑니다.
        # K에 1을 더해줍니다.
        K += 1

        # 만약 K에 1을 더했을 때 9가 된다면
        if K == 9:
            # 다음 차례는 1이 되어야 하므로 K를 1로 초기화합니다.
            K = 1
