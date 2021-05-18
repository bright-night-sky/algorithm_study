# https://www.acmicpc.net/problem/7789

# readline을 사용하기 위해 import합니다.
from sys import stdin

# 첫째 줄에 여섯 자리의 기존 전화번호, 새로 추가되는 한 자리 번호를 공백으로 구분해 입력합니다.
# 기존 전화번호는 0으로 시작하지 않으며,
# 새로 추가되는 한 자리 번호는 0이 아닙니다.
origin_number, add_number = stdin.readline().rstrip().split(' ')

# 기존 전화번호의 제곱근 이하의 수 중 가장 가까운 자연수를 저장하는 변수를 선언합니다.
origin_number_root = int(int(origin_number) ** 0.5)

# 기존 전화번호 앞에 새로 추가되는 한 자리 번호를 붙이고 정수형으로 변환해서 저장하는 변수를 선언합니다.
new_number = int(add_number + origin_number)
# new_number의 제곱근 이하의 수 중 가장 가까운 자연수를 저장하는 변수를 선언합니다.
new_number_root = int(new_number ** 0.5)

# 원래 전화번호와 새로운 전화번호가 소수인지 아닌지를 저장하는 변수를 선언합니다.
# Yes로 초기화합니다.
all_is_prime = "Yes"

# 원래 전화번호가 소수인지 판별해봅니다.
# 2부터 origin_number_root까지 반복해봅니다.
for number in range(2, origin_number_root + 1):
    # origin_number가 현재 숫자에 나누어 떨어진다면
    if int(origin_number) % number == 0:
        # 소수가 아니므로 all_is_prime에 No를 저장합니다.
        all_is_prime = "No"

# 새로운 전화번호가 소수인지 판별해봅니다.
# 2부터 new_number_root까지 반복해봅니다.
for number in range(2, new_number_root + 1):
    # new_number가 현재 숫자에 나누어 떨어진다면
    if new_number % number == 0:
        # 소수가 아니므로 all_is_prime에 No를 저장합니다.
        all_is_prime = "No"

# all_is_prime에 저장된 값을 출력합니다.
print(all_is_prime)