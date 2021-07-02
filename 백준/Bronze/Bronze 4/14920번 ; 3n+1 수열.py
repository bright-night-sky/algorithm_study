# https://www.acmicpc.net/problem/14920

# readline을 사용하기 위해 import합니다.
from sys import stdin


# C(1)을 입력합니다.
# 1 <= C(1) <= 100,000
# 정수형으로 변환합니다.
C = int(stdin.readline())

# 수열의 n을 저장하는 변수를 선언합니다.
n = 1
# 수열에서 1을 찾을 때까지 반복합니다.
while True:
    # 처음으로 1이 나온다면
    if C == 1:
        # 1의 n을 출력합니다.
        print(n)
        # 1을 찾았으므로 반복문을 탈출합니다.
        break

    # C(n)이 짝수일 때
    if C % 2 == 0:
        # C(n+1) = C(n)/2를 계산해줍니다.
        C //= 2
    # C(n)이 홀수일 때
    else:
        # C(n+1) = 3*C(n)+1을 계산해줍니다.
        C = 3 * C + 1

    # n에 1을 더해줍니다.
    n += 1