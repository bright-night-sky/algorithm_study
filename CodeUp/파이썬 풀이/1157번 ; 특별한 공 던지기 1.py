# https://codeup.kr/problem.php?id=1157

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 슬기가 던진 공의 위치를 입력합니다.
# 실수형으로 변환합니다.
ball_position = float(stdin.readline())

# 슬기가 던진 공의 위치가 50 이상 60 이하이면
if 50 <= ball_position <= 60:
    # win을 출력합니다.
    print('win')
# 그 외에는
else:
    # lose를 출력합니다.
    print('lose')