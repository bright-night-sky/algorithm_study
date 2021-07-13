# https://codeup.kr/problem.php?id=6040

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 2개의 정수 a, b를 공백으로 구분해 입력합니다.
# 각각 정수형으로 변환합니다.
a, b = map(int, stdin.readline().split(' '))

# a를 b로 나눈 몫을 출력합니다.
print(a // b)