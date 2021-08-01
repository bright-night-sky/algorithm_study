# https://codeup.kr/problem.php?id=6065

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 3개의 정수를 공백을 두고 입력합니다.
# 각각 정수형으로 변환하고 a, b, c 변수에 넣어줍니다.
a, b, c = map(int, stdin.readline().split(' '))

# a의 값이 짝수라면
if a % 2 == 0:
    # a의 값을 출력합니다.
    print(a)

# b의 값이 짝수라면
if b % 2 == 0:
    # b의 값을 출력합니다.
    print(b)

# c의 값이 짝수라면
if c % 2 == 0:
    # c의 값을 출력합니다.
    print(c)