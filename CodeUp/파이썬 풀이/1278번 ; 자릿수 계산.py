# https://codeup.kr/problem.php?id=1278

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 자연수 n을 입력합니다.
# 1 이상이며 int 범위입니다.
# 맨 끝의 \n은 떼어줍니다.
n = stdin.readline().rstrip()

# 입력한 n의 자릿수인 n의 길이를 출력합니다.
print(len(n))