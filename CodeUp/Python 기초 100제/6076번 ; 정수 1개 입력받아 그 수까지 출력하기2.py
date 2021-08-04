# https://codeup.kr/problem.php?id=6076

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 0 ~ 100 중 정수 1개를 입력합니다.
# 정수형으로 변환합니다.
num = int(stdin.readline())

# 0부터 num의 값까지 반복합니다.
for i in range(num + 1):
    # 현재 수인 i의 값을 출력합니다.
    print(i)