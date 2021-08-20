# https://codeup.kr/problem.php?id=1149

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 두 정수를 공백으로 구분해 입력합니다.
# 각각 정수형으로 변환합니다.
num1, num2 = map(int, stdin.readline().split())

# 두 정수 중 큰 정수를 출력합니다.
print(num1 if num1 > num2 else num2)