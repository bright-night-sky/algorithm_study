# https://codeup.kr/problem.php?id=6048

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 두 정수를 공백으로 구분해 입력합니다.
# 각각 정수형으로 만들어주고 변수에 넣어줍니다.
a, b = map(int, stdin.readline().split(' '))

# a가 b보다 작다면
if a < b:
    # True를 출력합니다.
    print(True)
# 그렇지 않다면, 즉, a가 b보다 작지 않다면
else:
    # False를 출력합니다.
    print(False)