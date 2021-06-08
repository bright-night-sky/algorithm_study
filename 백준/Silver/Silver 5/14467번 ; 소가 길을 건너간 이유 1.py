# https://www.acmicpc.net/problem/14467

# readline을 사용하기 위해 import합니다.
from sys import stdin

# 첫 줄에 관찰 횟수 N을 입력합니다.
# 100 이하의 양의 정수입니다.
# 정수형으로 변환합니다.
N = int(stdin.readline())
# 소들의 위치를 저장하는 리스트 변수를 선언합니다.
# 소의 번호는 1 이상 10 이하의 정수이므로 10번까지 있습니다.
# 아직 위치가 정해져있지 않으므로 각각 None으로 초기화해줍니다.
cows = [None] * 10
# 소가 길을 건너간 최소 횟수를 저장할 변수를 선언합니다.
cross_cnt = 0

# 관찰 횟수 N만큼 반복합니다.
for watch_idx in range(N):
    # 소의 번호와 위치를 공백으로 구분해 입력합니다.
    # 위치는 0 또는 1입니다.
    # 각각 정수형으로 변환합니다.
    cow_num, left_right = map(int, stdin.readline().split(' '))
    # 소의 이전 위치를 저장하는 변수를 선언합니다.
    prev_cow_position = cows[cow_num - 1]
    # 이번에 입력된 소의 번호에 입력된 위치로 초기화해줍니다.
    cows[cow_num - 1] = left_right

    # 소의 위치가 None이 아니면서
    # 이전의 위치와 현재의 위치가 다르다면
    if prev_cow_position != None and prev_cow_position != left_right:
        # 소가 이동한 것이므로 cross_cnt에 1을 더해줍니다.
        cross_cnt += 1

# 소가 길을 건너간 최소 횟수를 출력합니다.
print(cross_cnt)