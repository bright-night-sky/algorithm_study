# https://codeup.kr/problem.php?id=6051

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 두 정수를 공백을 두고 입력합니다.
# 각각 정수형으로 변환하고 변수에 넣어줍니다.
a, b = map(int, stdin.readline().split(' '))

# a와 b의 값이 다르다면
if a != b:
    # True를 출력합니다.
    print(True)
# 그렇지 않다면, 즉, a와 b의 값이 같다면
else:
    # False를 출력합니다.
    print(False)