# https://codeup.kr/problem.php?id=1351

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 시작 단과 마지막 단을 공백으로 구분해 입력합니다.
# 시작 단과 마지막 단은 정수 1 ~ 9입니다.
# 각각 int형으로 변환합니다.
start, end = map(int, stdin.readline().split())

# 시작 단부터 마지막 단까지 반복합니다.
for dan in range(start, end + 1):
    # 현재 단에서 1에서 9까지 반복합니다.
    for num in range(1, 10):
        # 출력 형식에 맞게 한 줄에 구구단 한 줄씩 출력합니다.
        print(f'{dan}*{num}={dan * num}')