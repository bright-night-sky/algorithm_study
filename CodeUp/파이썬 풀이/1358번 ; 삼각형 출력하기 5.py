# https://codeup.kr/problem.php?id=1358

# readline을 사용하기 위해 import합니다.
from sys import stdin


# n을 입력합니다.
# int형으로 변환합니다.
# n은 3부터 99까지의 홀수 중 하나입니다.
n = int(stdin.readline())

# 1부터 n까지 2를 건너뛰면서 반복합니다.
for num in range(1, n + 1, 2):
    # 삼각형 모양을 만들어주기 위해 먼저 공백을 출력합니다.
    # 공백을 (n - 현재 숫자) // 2만큼 출력하고, 다음 줄로 내리지 않습니다.
    print(' ' * ((n - num) // 2), end='')
    # 별 *들을 현재 숫자만큼 출력합니다.
    print('*' * num)