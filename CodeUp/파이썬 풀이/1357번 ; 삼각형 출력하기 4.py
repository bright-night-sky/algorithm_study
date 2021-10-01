# https://codeup.kr/problem.php?id=1357

# readline을 사용하기 위해 import합니다.
from sys import stdin


# n을 입력합니다.
# int형으로 변환합니다.
n = int(stdin.readline())

# 먼저 상단에 n줄의 삼각형을 출력합니다.
# n번 반복하는 반복문을 만듭니다.
for num in range(n):
    # 별 *들을 (현재 숫자 + 1)만큼 출력합니다.
    print('*' * (num + 1))

# 이어서 하단에 n-1줄의 역삼각형을 출력합니다.
# n-1부터 1까지 반복합니다.
for num in range(n - 1, 0, -1):
    # 별 *들을 현재 숫자만큼 출력합니다.
    print('*' * num)