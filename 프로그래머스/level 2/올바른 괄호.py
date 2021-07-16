# https://programmers.co.kr/learn/courses/30/lessons/12909

# '(' 또는 ')'로만 이루어진 문자열 s가 매개변수로 주어집니다.
# s의 길이는 100,000 이하의 자연수입니다.
def solution(s):
    # 올바른지 올바르지 않은 괄호인지 여부를 저장하는 변수를 선언합니다.
    # 올바른 괄호라는 뜻인 True로 초기화합니다.
    answer = True
    # '('를 저장할 괄호 스택 리스트 변수를 선언합니다.
    brackets = []

    # 문자열 s에 있는 괄호들을 하나씩 반복해봅니다.
    for bracket in s:
        # 현재 괄호가 '('라면
        if bracket == '(':
            # brackets에 현재 괄호 '('를 넣어줍니다.
            brackets.append(bracket)
        # 현재 괄호가 ')'인 경우
        else:
            # brackets가 빈 스택이라면
            if brackets == []:
                # 올바르지 않은 괄호이므로 answer에 False를 저장합니다.
                answer = False
                # 올바르지 않은 괄호로 확정되었으므로 반복문을 탈출합니다.
                break
            # brackets가 빈 스택이 아니라면
            else:
                # brackets의 맨 끝에 있는 '('를 하나 뺍니다.
                brackets.pop()

    # brackets가 빈 스택이 아니라면
    if brackets != []:
        # 올바르지 않은 괄호이므로 answer에 False를 저장합니다.
        answer = False

    # answer에 저장된 괄호의 상태를 반환합니다.
    return answer