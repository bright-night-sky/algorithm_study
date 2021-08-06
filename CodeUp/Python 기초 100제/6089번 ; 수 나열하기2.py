# https://codeup.kr/problem.php?id=6089

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 시작 값 a, 등비의 값 r, 몇 번째 인지를 나타내는 정수 n을 공백을 두고 입력합니다.
# 각각 정수형으로 변환합니다.
a, r, n = map(int, stdin.readline().split())

# 등비수열 공식을 이용하여 n번째 수를 구하고 출력합니다.
# 등비수열 공식 : an = a * r^(n-1)
print(a * (r ** (n - 1)))