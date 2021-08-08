# https://codeup.kr/problem.php?id=6098

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 10x10 크기의 미로 상자를 만들기 위한 10칸짜리 리스트를 선언합니다.
maze = [None] * 10
# 먹이의 x, y좌표를 저장할 변수를 선언합니다.
feed_x, feed_y = None, None

# 미로 상자의 구조와 먹이의 위치를 입력합니다.
# 10x10 크기에서 가로줄이 10개이므로 10번 반복합니다.
for idx in range(10):
    # 한 가로줄의 미로 구조를 공백으로 구분해 입력합니다.
    # 각각 정수형으로 변환하고 리스트로 만들어줍니다.
    # maze의 현재 인덱스에 리스트를 넣어줍니다.
    maze[idx] = list(map(int, stdin.readline().split()))

    # 이번에 입력한 가로줄에서 먹이값인 2가 있다면
    if 2 in maze[idx]:
        # 먹이의 x, y좌표값을 변수에 저장해줍니다.
        feed_x = idx
        feed_y = maze[idx].index(2)

# 현재 개미의 위치를 저장하는 변수들을 선언합니다.
# 미로 상자의 테두리는 모두 벽으로 되어 있으므로
# 개미가 출발하는 좌표는 인덱스 값으로 (1, 1)에서 시작합니다.
# 문제에서는 인덱스값 기준이 아니라 (2, 2)로 표시되어 있습니다.
cur_x, cur_y = 1, 1

# 계속 반복해봅니다.
while True:
    # 현재 개미 위치에서의 값을 저장하는 변수를 선언합니다.
    cur_num = maze[cur_x][cur_y]
    # 개미가 이동한 경로이므로 현재 위치의 값을 9로 변경합니다.
    maze[cur_x][cur_y] = 9

    # 현재 개미의 위치가 먹이의 위치였거나,
    # 개미가 맨 아래의 가장 오른쪽에 도착했거나,
    # 현재 개미의 위치에서 오른쪽과 밑이 모두 벽이라 더 이상 움직일 수 없다면
    if cur_num == 2 or (cur_x, cur_y) == (9, 9) or (maze[cur_x+1][cur_y] == 1 and maze[cur_x][cur_y+1] == 1):
        # 반복문을 탈출합니다.
        break

    # 현재 개미의 위치에서 오른쪽이 벽이라면
    if maze[cur_x][cur_y+1] == 1:
        # 개미는 밑으로 이동합니다.
        cur_x += 1
    # 그렇지 않다면
    else:
        # 개미는 오른쪽으로 이동합니다.
        cur_y += 1

# 반복문이 끝나고 난 뒤 개미가 이동한 경로를 9로 표시한 미로를 출력합니다.
for i in range(10):
    for j in range(10):
        # 미로에서 한 가로줄의 상황을 공백으로 구분해 출력합니다.
        print(maze[i][j], end=' ')
    # 한 가로줄의 상황이 모두 출력되면 다음 가로줄의 상황을 출력하기 위해 다음 줄로 넘어갑니다.
    print()