# https://codeup.kr/problem.php?id=6095

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 첫 줄에 바둑판에 올려 놓을 흰 돌의 개수 n을 입력합니다.
# 정수형으로 변환합니다.
n = int(stdin.readline())
# 아직 흰 돌을 놓은 상태가 아닌 상태,
# 즉, 모든 값이 0인 19x19 바둑판을 저장하는 2차원 리스트 변수를 선언합니다.
go_board = [[0 for j in range(19)] for i in range(19)]

# 흰 돌의 개수 n만큼 반복합니다.
for _ in range(n):
    # 흰 돌을 놓을 좌표 x, y를 공백을 두고 입력합니다.
    # 각각 정수형으로 변환합니다.
    x, y = map(int, stdin.readline().split())
    # 바둑판의 해당 좌표에 흰 돌을 놓았으므로, 해당 좌표의 값을 1로 변경합니다.
    go_board[x-1][y-1] = 1

# 바둑판의 상황을 출력하는 반복문을 만듭니다.
for i in range(19):
    for j in range(19):
        # 바둑판에서 한 가로줄의 상황을 공백으로 구분해 출력합니다.
        print(go_board[i][j], end=' ')
    # 한 가로줄의 상황이 모두 출력되면 다음 가로줄의 상황을 출력하기 위해 다음 줄로 넘어갑니다.
    print()