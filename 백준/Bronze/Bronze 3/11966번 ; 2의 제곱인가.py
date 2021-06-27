# https://www.acmicpc.net/problem/11966

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 첫째 줄에 N을 입력합니다.
# 1 <= N <= 2^30
# 정수형으로 변환합니다.
N = int(stdin.readline())

# 지수를 저장하는 변수를 선언합니다.
# 0부터 시작하므로 0으로 초기화합니다.
square = 0
# 계속 반복해봅니다.
while True:
    # N이 2의 제곱수인지 판별하기 위해 비교할 수를 저장하는 변수를 선언합니다.
    # 2에서 square에 저장된 숫자만큼 제곱한 값을 저장합니다.
    compare_num = 2 ** square

    # N과 compare_num이 같다면
    if N == compare_num:
        # N은 2의 제곱수이므로 1을 출력합니다.
        print(1)
        # 판별을 했으므로 반복문을 탈출합니다.
        break
    # N이 compare_num보다 작다면
    elif N < compare_num:
        # N은 2의 제곱수가 아니므로 0을 출력합니다.
        print(0)
        # 판별을 했으므로 반복문을 탈출합니다.
        break
    # N이 compare_num보다 크다면
    elif N > compare_num:
        # square에 1을 더합니다.
        square += 1