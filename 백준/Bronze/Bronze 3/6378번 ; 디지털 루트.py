# https://www.acmicpc.net/problem/6378

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 0을 입력할 때까지 반복합니다.
while True:
    # 양의 정수 N을 입력합니다.
    # 최대 1000자리입니다.
    # 맨 끝의 \n은 떼어줍니다.
    N = stdin.readline().rstrip()
    # N의 디지털 루트를 저장할 변수를 선언합니다.
    digital_root = None

    # 입력한 N이 0인 경우
    if N == '0':
        # 반복문을 탈출합니다.
        break

    # 디지털 루트를 구할 때까지 반복합니다.
    while True:
        # N의 모든 자리수를 더한 값을 digital_root 변수에 저장합니다.
        digital_root = str(sum(map(int, N)))

        # digital_root의 값의 길이가 1이라면
        if len(digital_root) == 1:
            # 디지털 루트를 구한 것이므로 그 값을 출력합니다.
            print(digital_root)
            # 반복문을 탈출합니다.
            break
        # digital_root의 값의 길이가 1이 아니라면
        else:
            # N에 digital_root의 값을 저장합니다.
            N = digital_root