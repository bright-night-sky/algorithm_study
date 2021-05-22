# https://www.acmicpc.net/problem/3028

# readline을 사용하기 위해 import합니다.
from sys import stdin

# 첫째 줄에 정인이가 컵을 섞은 순서를 입력합니다.
# A, B, C로 구성되어 있으며 최대 50번 섞습니다.
# 가장 왼쪽의 \n은 없애줍니다.
shuffle = stdin.readline().rstrip()

# 컵들에서 공의 위치를 저장하는 리스트 변수를 선언합니다.
# 공이 있는 컵은 True로 표시합니다.
ball_state = [True, False, False]

# 컵을 섞는 순서 하나씩 반복해봅니다.
for method in shuffle:
    # A 방법대로 컵을 섞는다면
    if method == 'A':
        # 왼쪽의 컵과 중앙에 있는 컵을 바꿔줍니다.
        ball_state[0], ball_state[1] = ball_state[1], ball_state[0]
    # B 방법대로 컵을 섞는다면
    elif method == 'B':
        # 중앙에 있는 컵과 오른쪽에 있는 컵을 바꿔줍니다.
        ball_state[1], ball_state[2] = ball_state[2], ball_state[1]
    # C 방법대로 컵을 섞는다면
    else:
        # 왼쪽에 있는 컵과 오른쪽에 있는 컵을 바꿔줍니다.
        ball_state[0], ball_state[2] = ball_state[2], ball_state[0]

# 공이 있는 위치를 출력해줍니다.
print(ball_state.index(True) + 1)