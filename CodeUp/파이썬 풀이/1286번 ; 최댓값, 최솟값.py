# https://codeup.kr/problem.php?id=1286

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 숫자를 하나 입력합니다.
# -1,000,000 ~ 1,000,000
# int형으로 변환하고 최댓값을 저장할 변수 max_num에 저장합니다.
max_num = int(stdin.readline())
# 입력한 값을 최솟값을 저장할 변수 min_num에도 저장합니다.
min_num = max_num

# 5개의 정수를 비교해야하므로 남은 네 번을 반복해봅니다.
for _ in range(4):
    # 숫자를 하나 입력합니다.
    # # -1,000,000 ~ 1,000,000
    # int형으로 변환합니다.
    num = int(stdin.readline())

    # 현재 입력한 숫자가 max_num의 값보다 크다면
    if num > max_num:
        # max_num에 현재 숫자의 값을 저장합니다.
        max_num = num

    # 현재 입력한 숫자가 min_num의 값보다 작다면
    if num < min_num:
        # min_num에 현재 숫자의 값을 저장합니다.
        min_num = num

# 입력한 5개의 정수 중 최댓값이 저장되어 있는 max_num의 값을 출력합니다.
print(max_num)
# 입력한 5개의 정수 중 최솟값이 저장되어 있는 min_num의 값을 출력합니다.
print(min_num)