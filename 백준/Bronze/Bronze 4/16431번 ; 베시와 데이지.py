# https://www.acmicpc.net/problem/16431

# 첫 번째 줄에 베시의 좌표 Br, Bc 입력
# 1 <= Br, Bc <= 1,000
Br, Bc = map(int, input().split(' '))

# 두 번째 줄에 데이지의 좌표 Dr, Dc 입력
# 1 <= Dr, Dc <= 1,000
Dr, Dc = map(int, input().split(' '))

# 세 번째 줄에 존의 좌표 Jr, Jc 입력
# 1 <= Jr, Jc <= 1,000
Jr, Jc = map(int, input().split(' '))

# 베시가 존의 좌표까지 이동하는데 걸리는 시간을 저장하는 변수
B_time = 0
# 데이지가 존의 좌표까지 이동하는데 걸리는 시간을 저장하는 변수
D_time = 0

# 베시가 존의 좌표까지 최대한 빨리 가려면 대각선으로 이동하는 것을 최대한 많이 해야한다.
# 베시가 대각선을 최대로 이동할 수 있는 횟수는 존의 좌표와의 가로 차이와 세로 차이 중 더 작은 숫자만큼이다.
width_gap = abs(Bc - Jc)
height_gap = abs(Br - Jr)
min_gap = min(width_gap, height_gap)
B_time = width_gap + height_gap - min_gap

# 데이지는 가로, 세로로만 한 번씩 이동할 수 있으므로
# 데이지가 존의 좌표까지 걸리는 시간은 데이지와 존의 좌표에서 각 좌표값의 차이를 더한 것이다.
D_time = abs(Dr - Jr) + abs(Dc - Jc)

# 베시가 더 빨리 도착하면
if B_time < D_time:
    # bessie 출력
    print("bessie")
# 데이지가 더 빨리 도착하면
elif B_time > D_time:
    # daisy 출력
    print("daisy")
# 동시에 도착하면
else:
    # tie 출력
    print("tie")