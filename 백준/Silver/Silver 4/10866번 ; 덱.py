# https://www.acmicpc.net/problem/10866

# readline을 사용하기 위해 import합니다.
from sys import stdin
# deque를 사용하기 위해 import합니다.
from collections import deque

# 첫째 줄에 명령의 수 N을 입력합니다.
# 1 <= N <= 10,000
# 정수형으로 변환합니다.
N = int(stdin.readline())
# 정수형 숫자들을 저장할 deque를 하나 선언합니다.
num_deque = deque()

# 명령의 수 N만큼 반복합니다.
for query_idx in range(N):
    # 명령을 한 줄 입력합니다.
    # 맨 끝의 \n을 떼고, 공백으로 구분해놓습니다.
    query = stdin.readline().rstrip().split(' ')

    # 명령의 맨 앞 단어가 push_front인 경우
    if query[0] == 'push_front':
        # num_deque의 앞에 정수 X인 query[1]를 넣습니다.
        num_deque.appendleft(int(query[1]))
    # 명령의 맨 앞 단어가 push_back인 경우
    elif query[0] == 'push_back':
        # num_deque의 뒤에 정수 X인 query[1]를 넣습니다.
        num_deque.append(int(query[1]))
    # 명령의 맨 앞 단어가 pop_front인 경우
    elif query[0] == 'pop_front':
        # num_deque가 비어있지 않다면
        if num_deque:
            # num_deque의 가장 앞에 있는 수를 빼고, 그 수를 출력합니다.
            print(num_deque.popleft())
        # num_deque가 비어있다면
        else:
            # -1을 출력합니다.
            print(-1)
    # 명령의 맨 앞 단어가 pop_back인 경우
    elif query[0] == 'pop_back':
        # num_deque가 비어있지 않다면
        if num_deque:
            # num_deque의 가장 뒤에 있는 수를 빼고, 그 수를 출력합니다.
            print(num_deque.pop())
        # num_deque가 비어있다면
        else:
            # -1을 출력합니다.
            print(-1)
    # 명령의 맨 앞 단어가 size인 경우
    elif query[0] == 'size':
        # num_deque에 들어있는 정수의 개수를 출력합니다.
        print(len(num_deque))
    # 명령의 맨 앞 단어가 empty인 경우
    elif query[0] == 'empty':
        # num_deque가 비어있지 않다면
        if num_deque:
            # 0을 출력합니다.
            print(0)
        # num_deque가 비어있다면
        else:
            # 1을 출력합니다.
            print(1)
    # 명령의 맨 앞 단어가 front인 경우
    elif query[0] == 'front':
        # num_deque가 비어있지 않다면
        if num_deque:
            # num_deque의 가장 앞에 있는 정수를 출력합니다.
            print(num_deque[0])
        # num_deque가 비어있다면
        else:
            # -1을 출력합니다.
            print(-1)
    # 명령의 맨 앞 단어가 back인 경우
    elif query[0] == 'back':
        # num_deque가 비어있지 않다면
        if num_deque:
            # num_deque의 가장 뒤에 있는 정수를 출력합니다.
            print(num_deque[-1])
        # num_deque가 비어있다면
        else:
            # -1을 출력합니다.
            print(-1)