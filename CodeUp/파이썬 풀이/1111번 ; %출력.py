# https://codeup.kr/problem.php?id=1111

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 정수 하나를 입력합니다.
# 맨 끝의 \n은 떼어줍니다.
num = stdin.readline().rstrip()

# 입력한 정수에 %를 붙여서 출력합니다.
print(num + '%')