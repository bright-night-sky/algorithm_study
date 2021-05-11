# https://www.acmicpc.net/problem/1459

# 첫째 줄에 집의 위치 X, Y와
# 한 블록 가는데 걸리는 시간 W,
# 대각선으로 한 블록을 가로지르는 시간 S 입력
# X, Y는 1,000,000,000보다 작거나 같은 음이 아닌 정수
# W, S는 10,000보다 작거나 같은 자연수
X, Y, W, S = map(int, input().split(' '))

# 대각선으로 한 블록을 가르는 최대 횟수는 X, Y 중 더 작은 값만큼만 가능하다.
possible_across_count = min(X, Y)

# 가로, 세로로 총 이동해야하는 횟수
total_distance = X + Y

# 최소시간을 저장하는 변수
min_time = 0

# 대각선으로 가로지르는 횟수를 0부터 가능한만큼 계산해본다.
for i in range(0, possible_across_count+1):
    #
    cur_time = 0
    # 대각선으로 가로지른만큼 소비한 시간을 계산한 변수
    across_time = i * S
    # 최종적으로 가야하는만큼의 거리에서 대각선으로 가로질러서 간 거리를 뺀 거리
    # 즉, 가로와 세로로 가야하는 거리
    not_across = total_distance - i * 2
    # 가로, 세로로 움직여서 소비한 시간을 계산
    not_across_time = not_across * W
    #
    cur_time = across_time + not_across_time

    # 만약 아직 최소시간에 아무런 값이 저장되어 있지 않았다면
    if min_time == 0:
        # 최소시간을 현재 계산한 시간으로 갱신
        min_time = cur_time

    # 직전까
    if cur_time <= min_time:
        min_time = cur_time

# 최종적으로 나오는 최소시간을 출력한다.
print(min_time)
