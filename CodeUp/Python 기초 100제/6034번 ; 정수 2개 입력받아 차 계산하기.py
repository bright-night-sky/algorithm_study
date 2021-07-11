# https://codeup.kr/problem.php?id=6034

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 2개의 정수를 공백으로 구분해 입력합니다.
# 각각 정수형으로 변환합니다.
num1, num2 = map(int, stdin.readline().split())

# 첫 번째 정수에서 두 번째 정수를 뺀 값을 출력합니다.
print(num1 - num2)