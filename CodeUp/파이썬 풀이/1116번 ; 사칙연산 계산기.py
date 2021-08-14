# https://codeup.kr/problem.php?id=1116

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 두 정수를 공백으로 구분해 입력합니다.
# 각각 정수형으로 변환합니다.
a, b = map(int, stdin.readline().split())

# 두 정수에 대한 사칙연산 결과를 출력 양식에 맞추어 출력합니다.
print(f'{a}+{b}={a + b}')
print(f'{a}-{b}={a - b}')
print(f'{a}*{b}={a * b}')
# 나눗셈은 소수점이 없게 그냥 몫으로만 표현합니다.
print(f'{a}/{b}={a // b}')