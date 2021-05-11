# https://www.acmicpc.net/problem/6246

# 첫 번째 줄에 슬롯 수 N과 풍선들을 꽂는 횟수 Q를 입력합니다.
# 1 <= N <= 10,000
# 1 <= Q <= 100
N, Q = map(int, input().split(' '))

# 슬롯 수 N개만큼 빈 슬롯 상태인 None으로 설정되어 있는 리스트 변수를 선언합니다.
balloon_state = [None for x in range(N)]

# 풍선들을 꽂는 횟수인 Q만큼 반복합니다.
for i in range(Q):
    # 풍선을 꽂는 방법인 두 정수 L, I를 입력합니다.
    # 1 <= L, I <= N
    L, I = map(int, input().split(' '))

    # L번 슬롯부터 I개씩 띄어서 풍선을 놓습니다.
    for index in range(L-1, N, I):
        # 놓은 자리의 리스트 변수에는 balloon이라는 문자열로 바꿔줍니다.
        balloon_state[index] = 'balloon'

# 슬롯 상태 변수에서 빈 슬롯 상태인 None의 개수를 저장하는 변수를 선언합니다.
blank_slot = balloon_state.count(None)

# 빈 슬롯의 개수를 출력합니다.
print(blank_slot)