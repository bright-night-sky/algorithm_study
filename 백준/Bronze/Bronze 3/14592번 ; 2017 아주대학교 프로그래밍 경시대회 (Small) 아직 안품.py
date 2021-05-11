# https://www.acmicpc.net/problem/14592

# 첫 번째 줄에는 참가자의 수 N을 입력합니다.
# 1 <= N <= 3
N = int(input())

#

# 참가자의 수만큼 돌려봅니다.
for i in range(1, N+1):
    # 참가자의 정보들인 Si, Ci, Li를 입력합니다.
    # Si : i번째 참가자의 점수, 0 <= Si <= 620
    # Ci : i번째 참가자의 제출 횟수, 0 <= Ci <= 50
    # Li : i번째 참가자의 마지막으로 점수를 획득한 문제의 업로드 시간, 0 <= Li <= 179
    # 세 값이 모두 같은 참가자는 없습니다.
    Si, Ci, Li = map(int, input().split(' '))

    # 현재 참가자의 번호를 저장하는 변수입니다.
    participant_id = i

