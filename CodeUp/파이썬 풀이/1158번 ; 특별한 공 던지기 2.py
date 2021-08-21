# https://codeup.kr/problem.php?id=1158

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 공의 위치 n을 입력합니다.
# 정수형으로 변환합니다.
n = int(stdin.readline())

# 공이 떨어지는 위치 n이 30 <= n <= 40이거나 60 <= n <= 70이면
if 30 <= n <= 40 or 60 <= n <= 70:
    # win을 출력합니다.
    print('win')
# 그 외에는
else:
    # lose를 출력합니다.
    print('lose')