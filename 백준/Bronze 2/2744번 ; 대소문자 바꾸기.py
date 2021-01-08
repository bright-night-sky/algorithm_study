# https://www.acmicpc.net/problem/2744

# 영어 소문자와 대문자로만 이루어진 단어 입력
# 단어 길이는 최대 100
string = input()

# 출력할 문자열 변수
result = ''

# 한 글자마다 소문자인지 대문자인지 구분
for one_char in string:
    # 소문자라면
    if one_char.islower():
        # 대문자로 변경해서 출력 문자열에 삽입
        result = result + one_char.upper()
    # 대문자라면
    else:
        # 소문자로 변경해서 출력 문자열에 삽입
        result = result + one_char.lower()

# 최종적으로 변경된 문자열 출력
print(result)
