# https://codeup.kr/problem.php?id=6044

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 정수 2개를 공백으로 구분해 입력합니다.
# 각각 정수형으로 변환합니다.
a, b = map(int, stdin.readline().split(' '))

# 두 정수의 합을 출력합니다.
print(a + b)
# 두 정수의 차를 출력합니다.
print(a - b)
# 두 정수의 곱을 출력합니다.
print(a * b)
# 두 정수의 몫을 출력합니다.
print(a // b)
# 두 정수의 나머지를 출력합니다.
print(a % b)
# 두 정수의 나눈 값을 출력합니다.
# 실수, 소수점 이하 둘째 자리까지의 정확도로 출력합니다.
print(format(a / b, '.2f'))