# https://codeup.kr/problem.php?id=6085

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 가로 해상도 w, 세로 해상도 h,
# 한 픽셀을 저장하기 위한 비트 b를 공백을 두고 입력합니다.
# 각각 정수형으로 변환합니다.
w, h, b = map(int, stdin.readline().split(' '))

# 필요한 저장 용량을 계산하고 소수점 셋째 자리에서 반올림하여 소수점 둘째 자리까지 표현합니다.
# w, h, b를 모두 곱하면 비트 단위이므로
# 바이트(byte) 단위로 변환하기 위해 8로 나누고 
# 킬로바이트(KB) 단위로 변환하기 위해 1024로 나누고
# 마지막으로 메가바이트(MB) 단위로 변환하기 위해 1024로 한 번 더 나눕니다.
need_capacity = format(w * h * b / 8 / 1024 / 1024, '.2f')

# 출력 형식에 맞게 출력합니다.
print(f'{need_capacity} MB')