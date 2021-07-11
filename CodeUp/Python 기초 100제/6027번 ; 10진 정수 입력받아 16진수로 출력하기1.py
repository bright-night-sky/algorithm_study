# https://codeup.kr/problem.php?id=6027

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 10진수 1개를 입력합니다.
# 정수형으로 변환합니다.
dec_num = int(stdin.readline())

# 입력한 10진수를 16진수로 변환합니다.
# 맨 앞의 0x는 떼어주고 출력합니다.
print(hex(dec_num)[2:])