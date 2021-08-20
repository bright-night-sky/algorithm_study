# https://codeup.kr/problem.php?id=1150

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 세 정수를 공백으로 구분해 입력합니다.
# 각각 정수형으로 변환합니다.
num1, num2, num3 = map(int, stdin.readline().split())

# min 내장 함수를 사용해 세 정수 중 가장 작은 값을 출력합니다.
print(min(num1, num2, num3))