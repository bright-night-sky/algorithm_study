# https://codeup.kr/problem.php?id=6053

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 정수 1개를 입력합니다.
# 정수형으로 변환하고, 이어서 불 자료형으로 변환합니다.
num = bool(int(stdin.readline()))

# 입력한 정수의 불 값이 False이면
if not num:
    # 입력한 정수의 불 값의 반대인 True를 출력합니다.
    print(not num)
# 입력한 정수의 불 값이 True이면
else:
    # 입력한 정수의 불 값의 반대인 False를 출력합니다.
    print(not num)