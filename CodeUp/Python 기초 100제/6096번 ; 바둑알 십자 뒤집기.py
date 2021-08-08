# https://codeup.kr/problem.php?id=6096

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 바둑알이 깔려 있는 상황을 만들기 위해 바둑판 변수를 만들어줍니다.
# 각 가로줄을 의미하는 길이 19의 None으로 초기화된 바둑판으로 만듭니다.
go_board = [None] * 19

# 처음에 바둑알이 깔려 있는 상황을 만들어줍니다.
# 19 x 19 크기이므로 가로줄 19번 반복해봅니다.
for idx in range(19):
    # 한 가로줄에 각 바둑알이 깔려 있는 상황을 공백으로 구분해 입력합니다.
    # 각각 정수형으로 변환하고 리스트 변수로 만들어줍니다.
    go_board[idx] = list(map(int, stdin.readline().split()))

# 십자 뒤집기 횟수 n을 입력합니다.
# 정수형으로 변환합니다.
n = int(stdin.readline())

# 십자 뒤집기 횟수 n만큼 반복합니다.
for _ in range(n):
    # 십자 뒤집기 좌표 x, y를 입력합니다.
    # 각각 정수형으로 변환합니다.
    x, y = map(int, stdin.readline().split())

    # 입력한 x에 해당하는 가로줄의 모든 바둑돌들을 1을 0으로, 0을 1로 뒤집습니다.
    # 리스트의 실제 인덱스는 0부터 시작하고, 좌표는 1부터 시작하므로 x에 1을 빼야합니다.
    go_board[x-1] = list(map(lambda rock: int(not rock), go_board[x-1]))

    # 입력한 y에 해당하는 세로줄의 모든 바둑돌들을 1을 0으로, 0을 1로 뒤집습니다.
    # 리스트의 실제 인덱스는 0부터 시작하고, 좌표는 1부터 시작하므로 y에 1을 빼야합니다.
    for idx in range(19):
        go_board[idx][y-1] = int(not go_board[idx][y-1])

# 바둑판의 상황을 출력하는 반복문을 만듭니다.
for i in range(19):
    for j in range(19):
        # 바둑판에서 한 가로줄의 상황을 공백으로 구분해 출력합니다.
        print(go_board[i][j], end=' ')
    # 한 가로줄의 상황이 모두 출력되면 다음 가로줄의 상황을 출력하기 위해 다음 줄로 넘어갑니다.
    print()