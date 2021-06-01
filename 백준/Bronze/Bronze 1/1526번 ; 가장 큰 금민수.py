# https://www.acmicpc.net/problem/1526

# readline을 사용하기 위해 import합니다.
from sys import stdin

# 첫째 줄에 N을 입력합니다.
# 4보다 크거나 같고 1,000,000보다 작거나 같은 자연수입니다.
# 정수형으로 변환합니다.
N = int(stdin.readline())

# 계속 반복합니다.
while True:
    # N의 길이가 N에서 4의 개수와 7의 개수의 합과 같다면
    if len(str(N)) == str(N).count('4') + str(N).count('7'):
        # N을 출력합니다.
        print(N)
        # 반복문을 탈출합니다.
        break

    # N에 1을 빼줍니다.
    N -= 1