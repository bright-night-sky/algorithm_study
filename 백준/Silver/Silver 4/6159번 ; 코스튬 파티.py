# https://www.acmicpc.net/problem/6159

# readline을 사용하기 위해 import합니다.
from sys import stdin

# 소의 수 N, 코스튬의 크기 S를 공백으로 구분해 입력합니다.
# 정수형으로 변환해서 저장합니다.
# 2 <= N <= 20,000
# 1 <= S <= 1,000,000
N, S = map(int, stdin.readline().split(' '))

# 소들의 크기를 저장하는 리스트 변수를 선언합니다.
cattle_sizes = []

# 코스튬에 들어갈 수 있는 서로 다른 소의 사이즈 짝의 개수를 저장하는 변수를 선언합니다.
pair_cnt = 0

# 소의 수 N만큼 반복해봅니다.
for cow_index in range(N):
    # 소 한 마리의 사이즈를 입력합니다.
    # 1보다 크거나 같고, 1,000,000보다 작거나 같습니다.
    cow_size = int(stdin.readline())
    # 입력한 소 한 마리의 사이즈를 cattle_sizes에 넣어줍니다.
    cattle_sizes.append(cow_size)

# 서로 다른 소들을 하나씩 뽑아봅니다.
for cow1 in range(N - 1):
    for cow2 in range(cow1 + 1, N):
        # 서로 다른 소들의 사이즈의 합이 코스튬의 크기보다 작거나 같다면
        if cattle_sizes[cow1] + cattle_sizes[cow2] <= S:
            # pair_cnt에 1을 더해줍니다.
            pair_cnt += 1

# pair_cnt를 출력해줍니다.
print(pair_cnt)