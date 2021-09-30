# https://codeup.kr/problem.php?id=1353

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 길이 n을 입력합니다.
# int형으로 변환합니다.
n = int(stdin.readline())

# 1부터 n까지 반복합니다.
for num in range(1, n + 1):
    # 별 *를 현재 숫자만큼 반복 출력합니다.
    print('*' * num)