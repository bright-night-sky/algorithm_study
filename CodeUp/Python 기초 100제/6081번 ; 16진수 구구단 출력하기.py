# https://codeup.kr/problem.php?id=6081

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 16진수로 한 자리 수를 입력합니다.
# A ~ F 중 하나입니다.
# 입력한 16진수 숫자를 10진수 숫자로 변환합니다.
hex_num = int(stdin.readline(), 16)

# 16진수 구구단을 출력하기 1부터 15까지 반복합니다.
for num in range(1, 16):
    # 현재 반복 중인 수에 맞는 16진수 곱셈 결과를 저장하는 변수를 선언합니다.
    # 대문자가 있는 16진수로 표현해줍니다.
    result = '%X' % (hex_num * num)
    # 출력 형식에 맞게 16진수 구구단 각각의 식을 출력합니다.
    # 영어 부분은 대문자로 출력합니다.
    print(f'{"%X" % hex_num}*{"%X" % num}={result}')