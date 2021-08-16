# https://codeup.kr/problem.php?id=1126

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 두 정수를 공백으로 분리하여 입력합니다.
# 각각 정수형으로 변환합니다.
a, b = map(int, stdin.readline().split())

# 더하기, 빼기, 곱하기, 몫, 나머지 연산을 출력 형식에 맞게 한 줄씩 출력합니다.
print(f'{a} + {b} = {a + b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a // b}')
print(f'{a} % {b} = {a % b}')