# https://codeup.kr/problem.php?id=6052

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 정수 1개를 입력합니다.
# 정수형으로 변환합니다.
num = int(stdin.readline())

# 입력한 값이 0이라면
if num == 0:
    # False를 출력합니다.
    print(False)
# 입력한 값이 0이 아니라면
else:
    # True를 출력합니다.
    print(True)