# https://codeup.kr/problem.php?id=1352

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 사각형의 길이 n을 입력합니다.
n = int(stdin.readline())

# 사각형의 세로 길이 n만큼 반복합니다.
for _ in range(n):
    # 현재 가로 줄에서 별 *를 n번만큼 반복해 출력합니다.
    print('*' * n)