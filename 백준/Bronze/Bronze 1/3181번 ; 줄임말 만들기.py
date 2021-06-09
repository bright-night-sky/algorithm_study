# https://www.acmicpc.net/problem/3181

# readline을 사용하기 위해 import합니다.
from sys import stdin

# 쓸모없는 단어들을 저장하는 튜플 변수를 선언합니다.
useless_words = ('i', 'pa', 'te', 'ni', 'niti', 'a', 'ali', 'nego', 'no', 'ili')

# 문장을 하나 입력합니다.
# 알파벳 소문자와 공백으로만 이루어져 있습니다.
# 최대 길이는 100입니다.
# 공백으로 구분해 단어로 분리한 후 리스트 변수에 넣습니다.
words = stdin.readline().rstrip().split(' ')
# 맨 앞에 있는 단어의 맨 앞 글자는 대문자로 변경한 후, 최종적인 줄임말을 저장할 변수에 초기화합니다.
abbreviation = words[0][0].upper()
# words의 맨 앞에 있는 단어는 빼줍니다.
words = words[1:]

# words에 있는 단어 하나씩 반복합니다.
for word in words:
    # 현재 단어가 쓸모없는 단어에 속하지 않는다면
    if word not in useless_words:
        # 현재 단어의 맨 앞 글자를 대문자로 변경하고 abbreviation에 넣어줍니다.
        abbreviation += word[0].upper()

# 최종적인 줄임말을 출력합니다.
print(abbreviation)