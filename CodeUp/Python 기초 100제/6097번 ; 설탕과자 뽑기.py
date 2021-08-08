# https://codeup.kr/problem.php?id=6097

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 첫 줄에 격자판의 세로 h, 가로 w를 공백을 두고 입력합니다.
# 각각 정수형으로 변환합니다.
h, w = map(int, stdin.readline().split())
# 두 번째 줄에 놓을 수 있는 막대의 개수 n을 입력합니다.
# 정수형으로 변환합니다.
n = int(stdin.readline())
# 아무 막대도 놓지 않은 처음의 격자판을 저장하는 2차원 리스트 변수를 만들어줍니다.
# 모두 0으로 초기화합니다.
board = [[0 for y in range(w)] for x in range(h)]

# 놓을 수 있는 막대의 개수 n만큼 반복합니다.
for _ in range(n):
    # 막대의 길이 l, 방향 d, 좌표 x, y를 공백을 두고 입력합니다.
    # 각각 정수형으로 변환합니다.
    l, d, x, y = map(int, stdin.readline().split())

    # 막대의 방향이 세로 즉, d의 값이 1이라면
    if d:
        # 좌표 x, y에서부터 세로 방향으로 막대의 길이 l만큼을 모두 1로 바꿉니다.
        for idx in range(x - 1, x - 1 + l):
            board[idx][y - 1] = 1
    # 막대의 방향이 가로 즉, d의 값이 0이라면
    else:
        # 좌표 x, y에서부터 가로 방향으로 막대의 길이 l만큼을 모두 1로 바꿉니다.
        board[x-1][y-1:y-1+d] = [1] * l

# 모든 막대를 놓은 격자판의 상태를 출력합니다.
for i in range(h):
    for j in range(w):
        # 격자판에서 한 가로줄의 상황을 공백으로 구분해 출력합니다.
        print(board[i][j], end=' ')
    # 한 가로줄의 상황이 모두 출력되면 다음 가로줄의 상황을 출력하기 위해 다음 줄로 넘어갑니다.
    print()