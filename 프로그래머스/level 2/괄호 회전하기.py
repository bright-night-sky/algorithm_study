# https://programmers.co.kr/learn/courses/30/lessons/76502

# 대괄호, 중괄호, 소괄호로 이루어진 문자열 s가 매개변수로 주어집니다.
def solution(s):
    # 올바른 괄호 문자열이 되게 하는 x의 개수를 저장할 변수를 선언합니다.
    # x의 개수는 올바른 괄호 문자열의 개수입니다.
    correct_brace_cnt = 0
    # 문자열 s의 길이를 저장하는 변수를 선언합니다.
    s_len = len(s)

    # 문자열 s의 길이만큼 왼쪽으로 x칸 회전합니다.
    for x_cnt in range(s_len):
        # 현재 x칸 회전한 문자열 s가 올바른 괄호 문자열인지 아닌지를 구별하기 위한 괄호 스택을 만들어줍니다.
        brace_stack = []
        # 현재 x칸 회전한 문자열 s가 올바른 괄호 문자열인지 아닌지를 저장할 변수를 선언합니다.
        # 처음에는 올바른 괄호 문자열이 맞다는 뜻인 True로 초기화합니다.
        is_correct_brace = True

        # 현재 x칸 회전한 문자열 s에서 한 문자씩 반복해봅니다.
        for idx in range(s_len):
            # 현재 괄호 문자를 저장하는 변수를 선언합니다.
            cur_brace = s[idx]

            # 현재 괄호 문자가 '(', '[', '{' 중 하나라면
            if cur_brace in ['(', '[', '{']:
                # brace_stack에 현재 괄호 문자를 넣어줍니다.
                brace_stack.append(cur_brace)
            # 현재 괄호 문자가 ')'라면
            elif cur_brace == ')':
                # try문을 시도해봅니다.
                try:
                    # brace_stack의 맨 끝 문자가 '('라면
                    if brace_stack[-1] == '(':
                        # 맨 끝 문자인 '('를 빼냅니다.
                        brace_stack.pop()
                # 예외가 발생한다면
                except:
                    # 현재 x칸 회전한 문자열 s는 올바른 괄호 문자열이 아니므로
                    # is_correct_brace에 False를 저장합니다.
                    is_correct_brace = False
                    # 올바른 괄호 문자열이 아니라고 확정되었으므로 반복문을 탈출합니다.
                    break
            # 현재 괄호 문자가 ']'라면
            elif cur_brace == ']':
                # try문을 시도해봅니다.
                try:
                    # brace_stack의 맨 끝 문자가 '['라면
                    if brace_stack[-1] == '[':
                        # 맨 끝 문자인 '['를 빼냅니다.
                        brace_stack.pop()
                # 예외가 발생한다면
                except:
                    # 현재 x칸 회전한 문자열 s는 올바른 괄호 문자열이 아니므로
                    # is_correct_brace에 False를 저장합니다.
                    is_correct_brace = False
                    # 올바른 괄호 문자열이 아니라고 확정되었으므로 반복문을 탈출합니다.
                    break
            # 현재 괄호 문자가 '}'라면
            elif cur_brace == '}':
                # try문을 시도해봅니다.
                try:
                    # brace_stack의 맨 끝 문자가 '{'라면
                    if brace_stack[-1] == '{':
                        # 맨 끝 문자인 '{'를 빼냅니다.
                        brace_stack.pop()
                # 예외가 발생한다면
                except:
                    # 현재 x칸 회전한 문자열 s는 올바른 괄호 문자열이 아니므로
                    # is_correct_brace에 False를 저장합니다.
                    is_correct_brace = False
                    # 올바른 괄호 문자열이 아니라고 확정되었으므로 반복문을 탈출합니다.
                    break

        # is_correct_brace가 True이고, brace_stack이 빈 리스트라면
        if is_correct_brace and brace_stack == []:
            # 현재 x칸 회전한 문자열 s는 올바른 괄호 문자열이므로 correct_brace_cnt에 1을 더해줍니다.
            correct_brace_cnt += 1

        # 문자열 s를 왼쪽으로 1칸 회전해줍니다.
        s = s[1:] + s[0]

    # 문자열 s를 왼쪽으로 x칸만큼 회전하면서 생긴 올바른 괄호 문자열의 개수를 반환합니다.
    return correct_brace_cnt