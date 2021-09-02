# https://codeup.kr/problem.php?id=1252

# readline을 사용하기 위해 import합니다.
from sys import stdin


# n을 입력합니다.
# 1 <= n <= 100,000
# int형으로 변환합니다.
n = int(stdin.readline())

# 1부터 n까지 반복해봅니다.
for num in range(1, n + 1):
    # 현재 숫자를 출력하고, 다음 줄로 내리지 않고 한 칸만 띄어줍니다.
    print(num, end=' ')