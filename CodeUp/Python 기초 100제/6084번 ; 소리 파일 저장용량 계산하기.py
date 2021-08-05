# https://codeup.kr/problem.php?id=6084

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 1초 동안 마이크로 소리강약을 체크하는 횟수 h,
# 한 번 체크한 값을 저장할 때 사용하는 비트 수 b,
# 좌우 등 소리를 저장할 트랙 개수인 채널 개수 c,
# 녹음할 시간(초) s를 공백을 두고 입력합니다.
# 각각 정수형으로 변환하고 변수에 넣어줍니다.
h, b, c, s = map(int, stdin.readline().split(' '))

# 필요한 저장 용량을 계산하고 소수점 첫째 자리까지의 정확도로 표현합니다.
# h, b, c, s를 모두 곱하면 비트 단위이므로
# 바이트(byte) 단위로 변환하기 위해 8로 나누고
# 킬로바이트(KB) 단위로 변환하기 위해 1024로 나누고
# 마지막으로 메가바이트(MB) 단위로 변환하기 위해 1024로 한 번 더 나눕니다.
need_capacity = format(h * b * c * s / 8 / 1024 / 1024, '.1f')

# 출력 형식에 맞게 출력합니다.
print(f'{need_capacity} MB')