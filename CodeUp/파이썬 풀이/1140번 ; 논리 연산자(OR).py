# https://codeup.kr/problem.php?id=1140

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 두 정수를 공백으로 구분해 입력합니다.
# 각각 정수형으로 변환합니다.
num1, num2 = map(int, stdin.readline().split())

# 입력한 두 정수 중 하나라도 1이라면
if num1 or num2:
    # 1을 출력합니다.
    print(1)
# 입력한 두 정수가 모두 0이라면
else:
    # 0을 출력합니다.
    print(0)