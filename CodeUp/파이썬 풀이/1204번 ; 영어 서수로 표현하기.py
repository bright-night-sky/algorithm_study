# https://codeup.kr/problem.php?id=1204

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 1 ~ 99 중 한 정수를 입력합니다.
# int형으로 변환합니다.
num = int(stdin.readline())
# 입력한 정수의 일의 자리 숫자를 저장하는 변수를 선언합니다.
ones_place_num = num % 10

# 입력한 정수가 11에서 13이라면
if 11 <= num <= 13:
    # 입력한 숫자 뒤에 문자열 'th'를 붙이고 출력합니다.
    print(f'{num}th')
# 입력한 숫자의 일의 자리 숫자가 1이라면
elif ones_place_num == 1:
    # 입력한 숫자 뒤에 문자열 'st'를 붙이고 출력합니다.
    print(f'{num}st')
# 입력한 숫자의 일의 자리 숫자가 2라면
elif ones_place_num == 2:
    # 입력한 숫자 뒤에 문자열 'nd'를 붙이고 출력합니다.
    print(f'{num}nd')
# 입력한 숫자의 일의 자리 숫자가 3이라면
elif ones_place_num == 3:
    # 입력한 숫자 뒤에 문자열 'rd'를 붙이고 출력합니다.
    print(f'{num}rd')
# 그 외의 경우에는
else:
    # 입력한 숫자 뒤에 문자열 'th'를 붙이고 출력합니다.
    print(f'{num}th')