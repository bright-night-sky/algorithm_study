# https://codeup.kr/problem.php?id=1180

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 휴지통의 자동 압축 기준인 수치 n을 입력합니다.
# 1 <= n <= 99
# 정수형으로 변환합니다.
n = int(stdin.readline())
# n의 일의 자리 숫자를 계산하고 변수에 저장합니다.
ones_place_num = n % 10
# n의 십의 자리 숫자를 계산하고 변수에 저장합니다.
tens_place_num = n // 10
# 압축하는 알고리즘에 따라 n의 십의 자리 숫자와 일의 자리 숫자를 바꾼 값을 먼저 계산하고,
# 휴지통을 압축했을 때의 양을 저장할 변수에 저장합니다.
compact_result = ones_place_num * 10 + tens_place_num
# n에서 십의 자리 숫자와 일의 자리 숫자를 바꾼 값인 현재 compact_result의 값에 2를 곱하고 다시 저장합니다.
compact_result *= 2

# compact_result가 100 이상이라면
if compact_result >= 100:
    # 100으로 나눈 나머지만 compact_result에 저장해 100의 자리 숫자는 무시합니다.
    compact_result %= 100

# 휴지통을 압축했을 때의 양인 compact_result의 값을 출력합니다.
print(compact_result)

# compact_result의 값이 50 이하라면
if compact_result <= 50:
    # 문자열 'GOOD'을 출력합니다.
    print('GOOD')
# 50을 초과하면
else:
    # 문자열 'OH MY GOD'을 출력합니다.
    print('OH MY GOD')