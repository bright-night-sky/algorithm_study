# https://codeup.kr/problem.php?id=6023

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 시:분:초 형식으로 시간을 입력합니다.
# :를 기준으로 나눠 리스트 변수로 만들어줍니다.
time_input = stdin.readline().rstrip().split(':')

# 분을 출력합니다.
print(time_input[1])