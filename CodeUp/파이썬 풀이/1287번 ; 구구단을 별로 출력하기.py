# https://codeup.kr/problem.php?id=1287

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 구구단의 n단을 입력합니다.
# 1 <= n <= 9
# int형으로 변환합니다.
n = int(stdin.readline())

# n단의 1부터 9까지 반복해봅니다.
for num in range(1, 10):
    # 별 '*'을 n X (현재 숫자)만큼 반복해서 출력합니다.
    print('*' * n * num)