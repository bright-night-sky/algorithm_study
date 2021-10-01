# https://codeup.kr/problem.php?id=1356

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 길이 n을 입력합니다.
# n >= 3
# int형으로 변환합니다.
n = int(stdin.readline())

# n번 반복하는 반복문을 만듭니다.
for num in range(n):
    # 사각형의 첫 번째 줄이거나 마지막 줄이라면
    if num == 0 or num == n - 1:
        # 별 *를 n개만큼 반복해서 출력합니다.
        print('*' * n)
    # 그 외의 경우
    else:
        # 처음 별 *를 하나 출력하고, 다음 줄로 내리지 않습니다.
        print('*', end='')
        # 공백을 n-2개만큼 반복 출력하고, 다음 줄로 내리지 않습니다.
        print(' ' * (n - 2), end='')
        # 마지막 별 *를 하나 출력합니다.
        print('*')