# https://codeup.kr/problem.php?id=6066

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 3개의 정수를 공백을 두고 입력합니다.
# 각각 정수형으로 변환하고, a, b, c 변수에 넣어줍니다.
a, b, c = map(int, stdin.readline().split(' '))

# a의 값이 짝수라면
if a % 2 == 0:
    # even을 출력합니다.
    print("even")
# 그 외의 경우라면
else:
    # odd를 출력합니다.
    print("odd")

# b의 값이 짝수라면
if b % 2 == 0:
    # even을 출력합니다.
    print("even")
# 그 외의 경우라면
else:
    # odd를 출력합니다.
    print("odd")

# c의 값이 짝수라면
if c % 2 == 0:
    # even을 출력합니다.
    print("even")
# 그 외의 경우라면
else:
    # odd를 출력합니다.
    print("odd")