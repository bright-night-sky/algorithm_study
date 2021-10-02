# https://codeup.kr/problem.php?id=1360

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 길이 n을 입력합니다.
# 1 <= n <= 99
# int형으로 변환합니다.
n = int(stdin.readline())

# 숫자 피라미드의 각 줄에서 출력할 숫자와 그 숫자의 개수를 의미하는 숫자들을
# n부터 1까지 1씩 줄여가면서 반복합니다.
for num in range(n, 0, -1):
    # 현재 숫자와 공백을 현재 숫자만큼 출력합니다.
    print(f'{num} ' * num)