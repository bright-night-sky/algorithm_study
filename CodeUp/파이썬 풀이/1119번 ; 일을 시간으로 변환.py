# https://codeup.kr/problem.php?id=1119

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 일(day)를 입력합니다.
# 정수형으로 변환합니다.
day = int(stdin.readline())

# 하루는 24시간이므로 day의 값에 24를 곱해 시간으로 변환하고 출력합니다.
print(day * 24)