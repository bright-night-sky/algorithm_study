# https://codeup.kr/problem.php?id=6050

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 두 정수를 공백을 두고 입력합니다.
# 각각 정수형으로 변환하고 변수에 넣어줍니다.
a, b = map(int, stdin.readline().split(' '))

# b가 a보다 크거나 같다면
if a <= b:
    # True를 출력합니다.
    print(True)
# 그렇지 않다면, 즉, b가 a보다 작다면
else:
    # False를 출력합니다.
    print(False)