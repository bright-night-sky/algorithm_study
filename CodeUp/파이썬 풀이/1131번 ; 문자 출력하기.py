# https://codeup.kr/problem.php?id=1131

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 문자 하나를 입력합니다.
# 맨 끝의 \n은 떼어줍니다.
char = stdin.readline().rstrip()

# 입력한 문자를 그대로 출력합니다.
print(char)