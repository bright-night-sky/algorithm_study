# https://codeup.kr/problem.php?id=1159

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 슬기가 던진 공의 위치를 입력합니다.
# 정수형으로 변환합니다.
ball_position = int(stdin.readline())

# 공의 위치가 50 이상 70 이하이거나, 6의 배수이면
if 50 <= ball_position <= 70 or ball_position % 6 == 0:
    # win을 출력합니다.
    print('win')
# 그 외에는
else:
    # lose를 출력합니다.
    print('lose')