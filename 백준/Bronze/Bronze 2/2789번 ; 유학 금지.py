# https://www.acmicpc.net/problem/2789

# CAMBRIDGE 알파벳들을 저장하는 리스트 변수를 선언합니다.
cambridge = ['C', 'A', 'M', 'B', 'R', 'I', 'D', 'G', 'E']

# 알파벳 대문자로 이루어진 단어를 입력합니다.
# 적어도 3글자이며, 많아야 100글자입니다.
word = input()

# 결과를 저장하는 변수를 선언합니다.
result = ''

# 입력한 단어에서 알파벳 하나씩 반복합니다.
for alphabet in word:
    # 현재 알파벳이 CAMBRIDGE에 속하지 않는다면
    if alphabet not in cambridge:
        # 현재 알파벳을 결과 변수에 넣어줍니다.
        result += alphabet

# 결과를 출력합니다.
print(result)