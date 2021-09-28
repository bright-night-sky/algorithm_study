# https://codeup.kr/problem.php?id=1296

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 철망의 길이 n을 입력합니다.
# int형으로 변환합니다.
n = int(stdin.readline())
# 직사각형이 최대 넓이를 가지려면 가로와 세로의 길이가 같은 정사각형여야합니다.
# 따라서 가로, 세로의 길이를 구하고 가로와 세로 길이를 곱해 최대 넓이를 구합니다.
# int형으로 만들어 소수점 이하는 버리고 정수로 만들어줍니다.
max_area = int((n / 4) ** 2)

# 최대 넓이인 max_area의 값을 출력합니다.
print(max_area)