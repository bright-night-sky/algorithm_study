# https://codeup.kr/problem.php?id=6047

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 정수 2개를 공백으로 구분해 입력합니다.
# 각각 정수형으로 만들어줍니다.
a, b = map(int, stdin.readline().split(' '))

# a를 2^b만큼 곱한 값을 구하고 출력합니다.
print(a << b)