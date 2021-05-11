# https://www.acmicpc.net/problem/20362

# readline을 사용하기 위해 import합니다.
from sys import stdin

# 첫 번째 줄에 채팅 개수 N, 정답자의 닉네임 S를 공백으로 구분해 입력합니다.
# 2 <= N <= 1,000
N, S = stdin.readline().rstrip().split(' ')
# N은 정수형으로 변환해줍니다.
N = int(N)

# N개의 채팅 기록을 저장할 리스트 변수를 선언합니다.
chatting_log = []
# 정답자가 입력한 정답을 저장할 변수를 선언합니다.
answer = ''

# 채팅 개수 N만큼 반복합니다.
for chatting_idx in range(N):
    # 닉네임과 채팅 내용이 공백으로 구분된 채팅 기록을 입력합니다.
    # 각 닉네임과 채팅 내용은 길이가 1 이상 10 이하이며
    # 알파벳 소문자로만 이루어져 있습니다.
    chatting_info = stdin.readline().rstrip().split(' ')

    # 입력한 채팅 내용에서 정답자가 나온다면
    if chatting_info[0] == S:
        # answer에 정답자의 채팅을 저장합니다.
        answer = chatting_info[1]

    # 채팅 기록을 리스트 형태로 chatting_log에 넣어줍니다.
    chatting_log.append(chatting_info)

# 아쉬운 사람의 명수를 저장하는 변수를 선언합니다.
regretted_cnt = 0

# chatting_log를 읽을 때 인덱스를 저장하는 변수를 선언합니다.
chatting_idx = 0
# chatting_log를 하나씩 반복해봅니다.
while True:
    # chatting_log의 현재 인덱스에서 닉네임이 정답자와 같다면
    if chatting_log[chatting_idx][0] == S:
        # 반복문을 탈출합니다.
        break
    # chatting_log의 현재 인덱스에서 닉네임이 정답자와 같지 않을 때
    else:
        # 정답자의 답과 현재 채팅을 친 사람의 채팅 내용이 같다면
        if chatting_log[chatting_idx][1] == answer:
            # 아쉬운 사람의 명수에 1을 더해줍니다.
            regretted_cnt += 1

    # 인덱스를 1 더해줍니다.
    chatting_idx += 1

# 아쉬운 사람의 명수를 출력합니다.
print(regretted_cnt)