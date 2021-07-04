# https://www.acmicpc.net/problem/14592

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 첫 번째 줄에 참가자의 수를 나타내는 자연수 N을 입력합니다.
# 1 <= N <= 3
# 정수형으로 변환합니다.
N = int(stdin.readline())
# 각 참가자들의 정보들을 저장할 리스트 변수를 선언합니다.
participants_infos = [None] * N

# 참가자의 수 N만큼 반복합니다.
for participants_idx in range(N):
    # 참가자의 정보들인 참가자의 점수 Si, 제출 횟수 Ci,
    # 마지막으로 점수를 획득한 문제의 업로드 시간 Li를 공백으로 구분해 입력합니다.
    # 0 <= Si <= 620
    # 0 <= Ci <= 50
    # 0 <= Li <= 179
    # 각각 정수형으로 변환하고 리스트 변수에 넣어줍니다.
    participant_info = list(map(int, stdin.readline().split(' ')))
    # 참가자의 번호를 participant_info에 넣어줍니다.
    participant_info.append(participants_idx + 1)

    # participants_infos에 현재 참가자의 정보들인 participant_info를 넣어줍니다.
    participants_infos[participants_idx] = participant_info

# participants_infos의 값들을 순위를 정하는 기준으로 정렬합니다.
# 첫 번째 기준은 총 점수가 높은 참가자가 더 높은 순위인 내림차순,
# 두 번째 기준은 제출 횟수가 적은 참가자가 더 높은 순위인 오름차순,
# 세 번째 기준은 마지막으로 점수를 획득한 문제의 업로드 시간이 빠른 참가자가 더 높은 순위인 오름차순으로 정렬해줍니다.
participants_infos.sort(key=lambda info: (-info[0], info[1], info[2]))

# 가장 높은 순위의 참가자인 participants_infos의 맨 앞에 있는 참가자의 번호를 출력합니다.
print(participants_infos[0][3])