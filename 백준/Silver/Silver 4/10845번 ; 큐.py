# https://www.acmicpc.net/problem/10845

# readline을 사용하기 위해 import합니다.
from sys import stdin
# deque을 사용하기 위해 import합니다.
from collections import deque


# 첫째 줄에는 명령의 수 N을 입력합니다.
# 1 <= N <= 10,000
# 정수형으로 변환합니다.
N = int(stdin.readline())
# 정수를 저장하는 큐를 선언합니다.
# deque으로 구현합니다.
q = deque()

# 명령의 수 N개만큼 반복합니다.
for query_idx in range(N):
    # 명령을 하나 입력합니다.
    # 맨 끝의 \n은 떼어줍니다.
    # push X와 같이 공백이 있는 명령도 있으므로 공백으로 구분해줍니다.
    query = stdin.readline().rstrip().split(' ')

    # 명령이 push인 경우
    if query[0] == 'push':
        # 공백으로 구분해 입력한 정수를 q에 넣어줍니다.
        q.append(query[1])
    # 명령이 pop인 경우
    elif query[0] == 'pop':
        # q에 정수가 하나라도 있는 경우
        if len(q) != 0:
            # q에서 가장 앞에 있는 정수를 빼고 그 정수를 저장하는 변수를 선언합니다.
            num = q.popleft()
            # num을 출력합니다.
            print(num)
        # q에 정수가 하나라도 없다면
        else:
            # -1을 출력합니다.
            print(-1)
    # 명령이 size인 경우
    elif query[0] == 'size':
        # 큐에 들어있는 정수의 개수인 q의 길이를 출력합니다.
        print(len(q))
    # 명령이 empty인 경우
    elif query[0] == 'empty':
        # 큐가 비어있는 경우인 q의 길이가 0이라면
        if len(q) == 0:
            # 1을 출력합니다.
            print(1)
        # 큐가 비어있지 않다면
        else:
            # 0을 출력합니다.
            print(0)
    # 명령이 front인 경우
    elif query[0] == 'front':
        # 큐에 정수가 하나라도 있는 경우인 q의 길이가 0이 아니라면
        if len(q) != 0:
            # q의 가장 앞에 있는 정수를 출력합니다.
            print(q[0])
        # 큐에 정수가 하나도 없는 경우인 q의 길이가 0이라면
        else:
            # -1을 출력합니다.
            print(-1)
    # 명령이 back인 경우
    elif query[0] == 'back':
        # 큐에 정수가 하나라도 있는 경우인 q의 길이가 0이 아니라면
        if len(q) != 0:
            # q의 가장 뒤에 있는 정수를 출력합니다.
            print(q[-1])
        # 큐에 정수가 하나도 없는 경우인 q의 길이가 0이라면
        else:
            # -1을 출력합니다.
            print(-1)