# https://www.acmicpc.net/problem/4539

# readline을 사용하기 위해 import합니다.
from sys import stdin
# 사사오입 반올림을 사용하기 위해 import합니다.
import decimal

# 사사오입 반올림으로 반올림 모드를 변경합니다.
context = decimal.getcontext()
context.rounding = decimal.ROUND_HALF_UP

# 첫째 줄에 테스트 케이스의 개수 n을 입력합니다.
# 정수형으로 변환합니다.
n = int(stdin.readline())

# 테스트 케이스의 개수 n을 반복합니다.
for test_case_idx in range(n):
    # 정수 x를 입력합니다.
    # 맨 끝의 \n은 빼줍니다.
    # 0 <= x <= 99999999
    x = stdin.readline().rstrip()
    # 정수 x의 길이를 저장하는 변수를 선언합니다.
    x_len = len(x)

    # 반올림할 자릿수를 저장하는 변수를 선언합니다.
    # 일의 자리에서부터 반올림을 하므로 -1로 초기화해줍니다.
    round_position = -1
    # 정수 x의 길이 - 1만큼 반복합니다.
    for cnt in range(x_len - 1):
        # 현재 round_position의 값에 해당하는 자릿수에서 반올림을 하고
        # 문자열로 변환한 뒤 x에 다시 저장해줍니다.
        x = str(round(decimal.Decimal(x), round_position))
        # round_position에 1을 빼줘 반올림할 자릿수를 변경해줍니다.
        round_position -= 1

    # 반올림한 결과를 출력해줍니다.
    print("%d" % decimal.Decimal(x))