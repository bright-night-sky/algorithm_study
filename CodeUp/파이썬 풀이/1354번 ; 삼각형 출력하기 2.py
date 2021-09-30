# https://codeup.kr/problem.php?id=1354

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 길이 n을 입력합니다.
# int형으로 변환합니다.
n = int(stdin.readline())

# n부터 1까지 역순으로 반복합니다.
for num in range(n, 0, -1):
    # 별 *를 현재 숫자만큼 반복 출력합니다.
    print('*' * num)