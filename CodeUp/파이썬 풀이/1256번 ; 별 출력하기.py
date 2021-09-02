# https://codeup.kr/problem.php?id=1256

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 별의 개수 n을 입력합니다.
# 1 <= n <= 1,000
# int형으로 변환합니다.
n = int(stdin.readline())

# 별(*)을 n개만큼 출력합니다.
print('*' * n)