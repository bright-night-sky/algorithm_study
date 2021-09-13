# https://codeup.kr/problem.php?id=1273

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 자연수 N을 입력합니다.
# 1 <= N <= 10,000
# int형으로 변환합니다.
N = int(stdin.readline())

# 1부터 N까지 반복해봅니다.
for num in range(1, N + 1):
    # N을 현재 숫자로 나누었을 때 나머지가 0이라면
    if N % num == 0:
        # 현재 숫자는 N의 약수이므로 출력합니다.
        # 출력하고 나서 다음 줄로 내리지 않고 한 칸 띄어줍니다.
        print(num, end=' ')