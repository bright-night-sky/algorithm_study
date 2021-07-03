# https://www.acmicpc.net/problem/10419

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 첫 번째 줄에 창영이가 궁금한 경우의 수 T를 입력합니다.
# 1 <= T <= 100
# 정수형으로 변환합니다.
T = int(stdin.readline())

# 경우의 수 T만큼 반복합니다.
for test_case_idx in range(T):
    # 수업시간 d를 입력합니다.
    # 1 <= d <= 10,000인 정수입니다.
    # 정수형으로 변환합니다.
    d = int(stdin.readline())
    # 교수님이 지각할 수 있는 최대 시간 저장할 변수를 선언합니다.
    # 0으로 초기화합니다.
    t = 0

    # 지각할 수 있는 최대 시간을 구할 때까지 반복합니다.
    while True:
        # 교수님이 지각한 시간과 수업할 수 있는 시간의 합을 저장하는 변수를 선언합니다.
        late_and_lesson = t ** 2 + t

        # late_and_lesson이 수업시간보다 크다면
        if late_and_lesson > d:
            # 최대 t - 1만큼 지각할 수 있으므로 t - 1을 출력합니다.
            print(t - 1)
            # 지각할 수 있는 최대 시간을 구했으므로 반복문을 탈출합니다.
            break
        # late_and_lesson이 수업시간보다 작거나 같다면
        else:
            # t에 1을 더해줍니다.
            t += 1