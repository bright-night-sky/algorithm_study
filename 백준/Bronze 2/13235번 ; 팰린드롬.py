# https://www.acmicpc.net/problem/13235

# 길이가 20보다 작거나 같고 알파벳 소문자로 이루어진 단어를 입력합니다.
word = input()

# 입력한 단어가 팰린드롬이라면
if word == word[::-1]:
    # true를 출력합니다.
    print("true")
# 입력한 단어가 팰린드롬이 아니라면
else:
    # false를 출력합니다.
    print("false")