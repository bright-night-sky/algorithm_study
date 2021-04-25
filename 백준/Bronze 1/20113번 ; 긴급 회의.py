# https://www.acmicpc.net/problem/20113

# 첫째 줄에 플레이어의 수 N을 입력합니다.
# 3 <= N <= 100
N = int(input())

# 둘째 줄에 N개의 정수를 공백으로 구분해 입력합니다.
# i번째 정수 Xi는 i번 플레이어가 Xi번 플레이어에 투표했음을 의미합니다.
# 0이면 투표를 건너뛰었다는 의미입니다.
player_vote = list(map(int, input().split(' ')))

# 각 플레이어가 투표 받은 수를 저장하는 리스트 변수를 선언합니다.
voted_count = [0 for x in range(N)]

# 입력받은 플레이어의 투표만큼 반복해봅니다.
for vote in player_vote:
    # 현재 플레이어의 투표가 0이라면
    if vote == 0:
        # 투표를 건너뛰므로 그냥 넘어갑니다.
        continue
    # 현재 플레이어의 투표가 0이 아니라면
    else:
        # 숫자에 해당하는 플레이어에 투표수를 1 추가해줍니다.
        voted_count[vote-1] += 1

# 플레이어가 받은 투표수 중 최댓값을 저장하는 변수를 선언합니다.
max_vote_num = max(voted_count)

# 플레이어가 받은 투표수 중 최댓값이 2개 이상이거나
# 모든 플레이어가 투표를 건너뛰었다면
if voted_count.count(max_vote_num) >= 2 or max_vote_num == 0:
    # skipped를 출력합니다.
    print("skipped")
# 플레이어가 받은 투표수 중 최댓값이 1개라면
else:
    # 최대 투표수를 가진 플레이어의 번호를 출력합니다.
    print(voted_count.index(max_vote_num) + 1)
