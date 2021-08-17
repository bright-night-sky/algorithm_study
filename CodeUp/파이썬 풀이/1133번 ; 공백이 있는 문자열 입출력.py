# https://codeup.kr/problem.php?id=1133

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 공백이 포함된 문자열을 입력합니다.
# 최대 길이는 30입니다.
# 맨 끝의 \n은 떼어줍니다.
string = stdin.readline().rstrip()

# 입력한 공백이 포함된 문자열을 그대로 출력합니다.
print(string)