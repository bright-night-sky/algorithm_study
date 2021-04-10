# https://www.acmicpc.net/problem/7567

# 첫 줄에는 괄호문자로만 이루어진 문자열을 입력합니다.
# 문자열의 길이는 3 이상 50 이하입니다.
parentheses = input()

# 최종 높이를 저장할 변수 height를 선언합니다.
# 처음에 있는 그릇의 높이는 무조건 10cm이므로 10으로 초기화해놓습니다.
height = 10

# 입력된 괄호문자에서 2번째 문자부터 끝까지 반복해봅니다.
for i in range(1, len(parentheses)):
    # 만약 현재 괄호문자가 이전의 괄호문자와 똑같은 문자라면
    if parentheses[i-1] == parentheses[i]:
        # 높이에 5cm를 추가합니다.
        height += 5
    # 만약 현재 괄호문자가 이전의 괄호문자와 다른 문자라면
    else:
        # 높이에 10cm를 추가합니다.
        height += 10

# 최종의 높이를 출력합니다.
print(height)