# https://codeup.kr/problem.php?id=1112

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 두 정수를 공백으로 구분해 입력합니다.
# 각각 정수형으로 변환합니다.
num1, num2 = map(int, stdin.readline().split())

# 입력한 순서대로 공백으로 구분해 출력합니다.
print(num1, num2)