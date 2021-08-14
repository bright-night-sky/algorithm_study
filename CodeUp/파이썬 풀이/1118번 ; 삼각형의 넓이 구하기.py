# https://codeup.kr/problem.php?id=1118

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 밑변(a), 높이(b)를 공백으로 구분해 입력합니다.
# 각각 정수형으로 변환합니다.
a, b = map(int, stdin.readline().split())

# 삼각형의 넓이를 계산하고 소수 첫째 자리까지로 만든 뒤, 출력합니다.
print('%.1f' % (a * b / 2))