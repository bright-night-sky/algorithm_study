# https://codeup.kr/problem.php?id=6029

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 16진수 정수 1개를 입력합니다.
# 입력한 16진수 정수를 10진수로 변환합니다.
hex_num = int(stdin.readline(), 16)

# 10진수로 변환된 16진수를 8진수로 변환하고 앞의 0o는 떼어준 뒤 출력합니다.
print(oct(hex_num)[2:])