# https://www.acmicpc.net/problem/3034

# readline을 사용하기 위해 import합니다.
from sys import stdin

# 첫째 줄에 던진 성냥의 개수 N, 박스의 가로 크기 W, 세로 크기 H를 공백으로 구분해 입력합니다.
# 각각 정수형으로 변환해줍니다.
# 1 <= N <= 50
# 1 <= W, H <= 100
N, W, H = map(int, stdin.readline().split(' '))

# 박스의 대각선의 길이를 저장하는 변수를 선언합니다.
diagonal = (W ** 2 + H ** 2) ** 0.5

# 성냥의 개수 N만큼 반복합니다.
for match_idx in range(N):
    # 성냥 한 개의 길이를 입력합니다.
    # 정수형으로 변환해줍니다.
    # 길이는 1보다 크거나 같고 1000보다 작거나 같은 자연수입니다.
    match = int(stdin.readline())

    # 성냥의 길이가 박스의 가로 길이, 세로 길이, 대각선의 길이 중 하나보다 작거나 같다면
    if match <= W or match <= H or match <= diagonal:
        # 성냥이 박스에 들어갈 수 있으므로 DA를 출력합니다.
        print("DA")
    # 그 외의 경우에는
    else:
        # 성냥이 박스에 들어갈 수 없으므로 NE를 출력합니다.
        print("NE")