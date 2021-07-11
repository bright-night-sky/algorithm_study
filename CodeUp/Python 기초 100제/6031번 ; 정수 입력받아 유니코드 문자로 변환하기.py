# https://codeup.kr/problem.php?id=6031

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 10진수 정수 1개를 입력합니다.
# 32 ~ 126 범위의 정수입니다.
# 정수형으로 변환합니다.
num = int(stdin.readline())

# 해당 정수에 해당하는 유니코드 문자를 출력합니다.
print(chr(num))