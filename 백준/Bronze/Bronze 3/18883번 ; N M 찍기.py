# https://www.acmicpc.net/problem/18883

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 첫째 줄에 자연수 N, M을 공백으로 구분해 입력합니다.
# 두 수는 1,000보다 작거나 같은 자연수입니다.
# 각각 정수형으로 변환합니다.
N, M = map(int, stdin.readline().split(' '))
# 출력할 숫자를 저장하는 변수를 선언합니다.
# 1부터 출력하므로 1로 초기화합니다.
number = 1

# NXM 형식으로 출력하므로 먼저 행의 개수 N만큼 반복합니다.
for i in range(N):
    # 열의 개수 M만큼 반복합니다.
    for j in range(M):
        # 현재 열의 인덱스가 M-1보다 작다면
        if j < M - 1:
            # 숫자를 출력하고 오른쪽에 공백을 만듭니다.
            print(number, end=' ')
        # 현재 열의 인덱스가 M-1과 같다면
        # 즉, 열의 마지막 인덱스라면
        elif j == M - 1:
            # 숫자를 출력하고 자동 줄 바꿈은 하지 않습니다.
            print(number, end='')

        # 출력하는 숫자에 1을 더해줍니다.
        number += 1
    # 한 행의 출력이 다 끝나면 \n으로 줄바꿈을 합니다.
    print('\n', end='')