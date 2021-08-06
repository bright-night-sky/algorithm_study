# https://codeup.kr/problem.php?id=6088

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 시작 값 a, 등차의 값 d, 몇 번째 수인지를 의미하는 정수 n을 공백을 두고 입력합니다.
# 각각 정수형으로 변환합니다.
a, d, n = map(int, stdin.readline().split())

# 등차수열 공식을 이용하여 n번째 수를 구하고 출력합니다.
# 등차수열 공식 : an = a1 + (n-1)d
print(a + (n - 1) * d)