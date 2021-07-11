# https://codeup.kr/problem.php?id=6028

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 10진수 하나를 입력합니다.
# 정수형으로 변환합니다.
dec_num = int(stdin.readline())

# 입력한 10진수를 16진수로 변환하고 출력합니다.
# 영문은 대문자로 표현합니다.
print('%X' % dec_num)