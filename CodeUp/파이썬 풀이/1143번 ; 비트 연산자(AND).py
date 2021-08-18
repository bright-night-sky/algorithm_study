# https://codeup.kr/problem.php?id=1143

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 두 정수를 공백으로 구분해 입력합니다.
# 각각 정수형으로 변환합니다.
num1, num2 = map(int, stdin.readline().split())

# 두 정수를 비트단위로 AND 연산한 후 결과를 10진수로 출력합니다.
print(num1 & num2)