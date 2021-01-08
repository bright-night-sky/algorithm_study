# https://www.acmicpc.net/problem/1173

# N, m, M, T, R 입력
# N : 운동을 N분 동안 한다.
# m : 초기 맥박, 최소 맥박
# M : 최대 맥박, 이 맥박을 넘을 수 없다.
# T : 운동을 할 경우 증가하는 맥박량
# R : 휴식을 할 경우 감소하는 맥박량
# 1 <= N, T, R <= 200
# 50 <= m <= M <= 200
N, m, M, T, R = map(int, input().split(' '))

# 현재 맥박을 저장하는 변수
# 초기 맥박은 입력받은 m이다.
current_pulse = m

# 운동, 휴식 총 시간을 저장하는 변수
time = 0
# 운동만 한 시간을 저장하는 변수
exerciese_time = 0

# 운동 시작
while True:
    # 다만 운동을 N분 할 수 없는 경우도 있다.
    # (최소 맥박(m) + 운동 시 맥박 증가량(R)) > 최대 맥박(M) 경우 운동을 못한다.
    if (m + T) > M:
        # 운동을 N분 할 수 없으므로 -1을 출력할 것이다.
        time = -1
        # 반복문을 돌릴 필요 없으므로 탈출
        break

    # 현재 맥박이 최대 맥박보다 작으면 1분동안 운동을 한다.
    if (current_pulse + T) <= M:
        # 총 시간과 운동한 시간에 1분 추가
        time += 1
        exerciese_time += 1
        # 현재 맥박에 맥박 증가량을 추가
        current_pulse += T
    # 현재 맥박이 최대 맥박을 초과하면 1분 동안 휴식을 취한다.
    else:
        # 총 시간에 1분 추가
        time += 1
        # 현재 맥박에 맥박 감소량을 뺀다.
        current_pulse -= R
        # 다만 최소 맥박량 보다 작을 수는 없으므로 조정
        if current_pulse <= m:
            current_pulse = m

    # 목표로 한 N분 동안의 운동시간을 달성하면
    if exerciese_time == N:
        # 반복문 탈출
        break

# 목표로 한 운동 시간을 달성하는데 걸린 총 시간을 출력
print(time)
