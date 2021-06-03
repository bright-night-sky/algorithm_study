# https://www.acmicpc.net/problem/10828

# readline을 사용하기 위해 import합니다.
from sys import stdin

# 첫째 줄에 주어지는 명령의 수 N을 입력합니다.
# 1 <= N <= 10,000
# 정수형으로 변환합니다.
N = int(stdin.readline())
# 정수들을 저장하는 스택을 리스트 변수로 선언합니다.
stack = []

# 명령의 개수 N만큼 반복합니다.
for query_idx in range(N):
    # 명령을 입력합니다.
    # 정수 X를 입력할 때, 정수는 1보다 크거나 같고, 100,000보다 작거나 같습니다.
    query = stdin.readline().rstrip()

    # 입력한 명령에서 맨 앞 글자 4개가 push라면
    if query[:4] == 'push':
        # 입력한 명령에서 공백 뒤에 있는 정수 X를 저장하는 변수를 선언합니다.
        X = query.split(' ')[1]
        # X를 스택에 넣어줍니다.
        stack.append(X)
    # 입력한 명령이 pop이라면
    elif query == 'pop':
        # 스택이 비어있지 않다면
        if len(stack) != 0:
            # 스택에서 가장 위의 정수를 빼고, 그 수를 출력합니다.
            print(stack.pop())
        # 스택이 비어있다면
        else:
            # -1을 출력합니다.
            print(-1)
    # 입력한 명령이 size라면
    elif query == 'size':
        # 스택에 들어있는 정수의 개수를 출력합니다.
        print(len(stack))
    # 입력한 명령이 empty라면
    elif query == 'empty':
        # 스택이 비어있다면
        if len(stack) == 0:
            # 1을 출력합니다.
            print(1)
        # 스택이 비어있지 않다면
        else:
            # 0을 출력합니다.
            print(0)
    # 입력한 명령이 top라면
    elif query == 'top':
        # 스택이 비어있지 않다면
        if len(stack) != 0:
            # 스택의 가장 위에 있는 정수를 출력합니다.
            print(stack[-1])
        # 스택이 비어있다면
        else:
            # -1을 출력합니다.
            print(-1)