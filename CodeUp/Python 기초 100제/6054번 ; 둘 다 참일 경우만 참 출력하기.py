# https://codeup.kr/problem.php?id=6054

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 2개의 정수를 공백을 두고 입력합니다.
# 각각 정수형으로 변환합니다.
num1, num2 = map(int, stdin.readline().split(' '))

# 입력한 두 정수의 불 값이 모두 True라면
if bool(num1) and bool(num2):
    # True를 출력합니다.
    print(True)
# 그 외의 경우에는
else:
    # False를 출력합니다.
    print(False)