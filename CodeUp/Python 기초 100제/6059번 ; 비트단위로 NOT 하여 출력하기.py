# https://codeup.kr/problem.php?id=6059

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 정수 1개를 입력하고, 정수형으로 변환합니다.
num = int(stdin.readline())

# 비트 단위로 1과 0을 서로 바꾼 후, 10진수로 출력합니다.
print(~num)