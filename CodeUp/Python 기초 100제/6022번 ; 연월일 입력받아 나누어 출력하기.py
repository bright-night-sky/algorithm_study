# https://codeup.kr/problem.php?id=6022

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 6자리 숫자로 이루어진 연월일(YYMMDD)를 입력합니다.
# 맨 끝의 \n은 떼어줍니다.
yymmdd = stdin.readline().rstrip()

# 년도(YY)인 앞의 두 자리, 월(MM)인 중간의 두 자리, 일(DD)인 끝의 두 자리를 공백으로 구분해 출력합니다.
print(yymmdd[:2], yymmdd[2:4], yymmdd[4:])