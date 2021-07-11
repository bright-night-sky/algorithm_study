# https://codeup.kr/problem.php?id=6033

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 문자 1개를 입력합니다.
# 맨 끝의 \n은 떼어줍니다.
char = stdin.readline().rstrip()

# 입력한 문자 1개를 유니코드 숫자로 변환하고 1을 더한 뒤, 다시 문자로 변환한 것을 출력합니다.
print(chr(ord(char) + 1))