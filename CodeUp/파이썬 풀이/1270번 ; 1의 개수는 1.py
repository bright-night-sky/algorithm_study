# https://codeup.kr/problem.php?id=1270

# readline을 사용하기 위해 import합니다.
from sys import stdin


# n을 입력합니다.
# 1 <= n <= 1,000,000
# int형으로 변환합니다.
n = int(stdin.readline())
# 1부터 n까지의 수 중 맨 마지막 자리가 1인 수의 개수를 저장할 변수를 선언합니다.
# 0으로 초기화합니다.
last_one_cnt = 0

# 1부터 n까지 반복해봅니다.
for num in range(1, n + 1):
    # 현재 숫자의 마지막 숫자가 1이라면, 즉, 현재 숫자를 10으로 나누었을 때 나머지가 1이라면
    if num % 10 == 1:
        # last_one_cnt에 1을 더해줍니다.
        last_one_cnt += 1

# 맨 마지막 자리가 1인 수의 개수인 last_one_cnt의 값을 출력합니다.
print(last_one_cnt)