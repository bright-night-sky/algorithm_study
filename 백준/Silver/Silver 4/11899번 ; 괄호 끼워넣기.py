# https://www.acmicpc.net/problem/11899

# readline을 사용하기 위해 import합니다.
from sys import stdin

# 첫 번째 줄에 올바르지 않은 괄호열 S를 입력합니다.
# S의 길이는 1 이상 50 이하입니다.
# 맨 끝의 \n은 지워줍니다.
S = stdin.readline().rstrip()
# 괄호 스택을 리스트 변수로 선언합니다.
bracket_stack = []
# 필요한 괄호의 최소 개수를 저장하는 변수를 선언합니다.
need_bracket_cnt = 0

# 괄호열 S를 한 글자씩 반복해봅니다.
for bracket in S:
    # 현재 글자가 (라면
    if bracket == '(':
        # 괄호 스택에 (를 넣어줍니다.
        bracket_stack.append(bracket)
    # 현재 글자가 )라면
    else:
        # 괄호 스택이 비워져 있지 않고, 마지막 글자가 (라면
        if len(bracket_stack) != 0 and bracket_stack[-1] == '(':
            # 괄호 스택에서 마지막 글자인 (를 빼줍니다.
            bracket_stack.pop()
        # 그 외의 경우라면
        else:
            # 필요한 괄호의 개수에 1을 더해줍니다.
            need_bracket_cnt += 1

# 괄호 스택에 남아있는 (만큼 )가 필요하므로 그 개수를 필요한 괄호의 개수에 더해줍니다.
need_bracket_cnt += len(bracket_stack)
# 필요한 괄호의 최소 개수를 출력합니다.
print(need_bracket_cnt)