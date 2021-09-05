# https://codeup.kr/problem.php?id=1265

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 원하는 단을 입력합니다.
# 1 ~ 9
# int형으로 변환합니다.
dan = int(stdin.readline())

# 1부터 9까지 반복해봅니다.
for num in range(1, 10):
    # 출력 양식에 맞추어 입력한 단의 한 줄씩 출력합니다.
    print(f'{dan}*{num}={dan*num}')