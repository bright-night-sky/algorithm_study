# https://codeup.kr/problem.php?id=1147

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 두 정수 a, x를 입력합니다.
# 각각 정수형으로 변환합니다.
a, x = map(int, stdin.readline().split())

# a의 값을 x만큼 왼쪽으로 shift 연산한 결과를 출력합니다.
print(a << x)