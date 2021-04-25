# https://www.acmicpc.net/problem/20362

# 첫 번째 줄에 채팅 개수 N, 정답자의 닉네임 S를 공백으로 구분해 입력합니다.
# 2 <= N <= 1,000
N, S = input().split(' ')
N = int(N)

sorriness = 0

for chatting_log in range(N):
    nickname, chatting_content = input().split(' ')

