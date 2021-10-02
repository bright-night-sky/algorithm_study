# https://codeup.kr/problem.php?id=1359

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 길이 n을 입력합니다.
# int형으로 변환합니다.
# 1 <= n <= 99
n = int(stdin.readline())

# 숫자 피라미드의 줄과 해당 줄에서 마지막 숫자를
# 의미하는 num1을 1부터 n까지 반복합니다.
for num1 in range(1, n + 1):
    # 1부터 (현재 num1의 값 - 1)까지 반복합니다.
    for num2 in range(num1):
        # (현재 num2 + 1)의 값을 출력하고,
        # 다음 줄로 내리지 않고 한 칸만 띄웁니다.
        print(num2 + 1, end=' ')
    # 숫자 피라미드에서 한 줄 출력이 끝나면 다음 줄로 넘어갑니다.
    print()