# https://codeup.kr/problem.php?id=6035

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 2개의 실수들을 공백으로 구분해 입력합니다.
# 각각 실수형으로 변환합니다.
num1, num2 = map(float, stdin.readline().split(' '))

# 입력한 두 실수를 곱한 값을 출력합니다.
print(num1 * num2)