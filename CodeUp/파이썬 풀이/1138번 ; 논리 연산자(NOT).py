# https://codeup.kr/problem.php?id=1138

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 0 또는 1을 입력합니다.
# 정수형으로 변환합니다.
zero_or_one = int(stdin.readline())

# 입력한 0이나 1의 논리값을 반대로 바꾸고 정수형으로 변환해서 출력합니다.
print(int(not zero_or_one))