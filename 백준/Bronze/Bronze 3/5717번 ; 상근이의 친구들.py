# https://www.acmicpc.net/problem/5717

# readline을 사용하기 위해 import합니다.
from sys import stdin

# 계속 반복해봅니다.
while True:
    # 남자 친구의 수 M, 여자 친구의 수 F를 공백으로 구분해 입력합니다.
    # 각각 정수로 변환합니다.
    # 1 <= M, F <= 5
    M, F = map(int, stdin.readline().split(' '))

    # M, F가 모두 0이라면
    if M == F == 0:
        # 반복문을 탈출합니다.
        break
    # M, F가 하나라도 0이 아니라면
    else:
        # M과 F의 합을 출력합니다.
        print(M + F)