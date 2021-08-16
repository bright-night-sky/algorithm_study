# https://codeup.kr/problem.php?id=1125

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 10진수 정수 하나를 입력합니다.
# 정수형으로 변환합니다.
dec_num = int(stdin.readline())

# 8진수와 16진수를 공백으로 구분하고 차례대로 출력합니다.
# 16진수는 대문자로 출력합니다.
print('%o' % dec_num, '%X' % dec_num)