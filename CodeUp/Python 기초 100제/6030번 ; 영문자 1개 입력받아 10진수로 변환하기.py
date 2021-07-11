# https://codeup.kr/problem.php?id=6030

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 유니코드 영문자 1개를 입력합니다.
# 맨 끝의 \n은 떼어줍니다.
char = stdin.readline().rstrip()

# 입력한 영문자에 대한 유니코드 값을 10진수로 출력합니다.
print(ord(char))