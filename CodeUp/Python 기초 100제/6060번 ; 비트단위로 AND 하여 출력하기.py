# https://codeup.kr/problem.php?id=6060

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 정수 2개를 공백을 두고 입력합니다.
# 각각 정수형으로 변환합니다.
num1, num2 = map(int, stdin.readline().split(' '))

# 두 정수를 비트단위로 and 계산하고 그 결과를 10진수로 출력합니다.
print(num1 & num2)