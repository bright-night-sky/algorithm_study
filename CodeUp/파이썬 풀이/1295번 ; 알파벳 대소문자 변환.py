# https://codeup.kr/problem.php?id=1295

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 한 줄의 공백없는 문장을 입력합니다.
# 최대 길이는 1000입니다.
# 맨 끝의 \n은 떼어줍니다.
string = stdin.readline().rstrip()

# 입력한 문장의 대소문자를 서로 변환한 결과를 출력합니다.
print(string.swapcase())