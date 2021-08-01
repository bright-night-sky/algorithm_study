# https://codeup.kr/problem.php?id=6058

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 2개의 정수를 공백을 두고 입력합니다.
# 각각 정수형으로 변환합니다.
num1, num2 = map(int, stdin.readline().split(' '))

# 두 정수의 불 값이 모두 False인 경우
if not bool(num1) and not bool(num2):
    # True를 출력합니다.
    print(True)
# 그 외의 경우
else:
    # False를 출력합니다.
    print(False)