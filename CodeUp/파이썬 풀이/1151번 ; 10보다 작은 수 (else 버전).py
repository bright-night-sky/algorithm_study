# https://codeup.kr/problem.php?id=1151

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 자연수 하나를 입력합니다.
# 정수형으로 변환합니다.
num = int(stdin.readline())

# 입력한 자연수가 10 미만이라면
if num < 10:
    # small을 출력합니다.
    print('small')