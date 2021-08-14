# https://codeup.kr/problem.php?id=1117

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 두 실수를 공백으로 구분해 입력합니다.
# 각각 실수형으로 변환합니다.
num1, num2 = map(float, stdin.readline().split())

# 두 실수의 곱을 구하고 소수 둘째자리까지로 만든 뒤, 출력합니다.
print('%.2f' % (num1 * num2))