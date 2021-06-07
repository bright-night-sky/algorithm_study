# https://www.acmicpc.net/problem/19844

# readline을 사용하기 위해 import합니다.
from sys import stdin

# 첫째 줄에 "문장"을 나타내는 문자열을 입력합니다.
# 맨 끝의 \n을 지워주고, 하이픈(-)을 공백으로 변경해줍니다.
string = stdin.readline().rstrip().replace('-', ' ')
# string을 공백 단위로 쪼개어 나온 단어들을 리스트 변수에 넣어줍니다.
words = string.split(' ')
# 어포스트로피가 있는 단어에서 맨 앞 부분이 c', j', n', m', t', s', l', d', qu', s'로
# 시작하는지 판별하기 위한 튜플 변수를 만들어줍니다.
front_word = ('c\'', 'j\'', 'n\'', 'm\'', 't\'', 's\'', 'l\'', 'd\'', 'qu\'', 's\'')
# 프랑스어의 모음인 a, e, i, o, u, h를 튜플로 만들어줍니다.
vowels = ('a', 'e', 'i', 'o', 'u', 'h')
# 총 단어의 개수를 저장할 변수를 선언합니다.
# 현재 하이픈과 공백으로 쪼개어 나온 단어의 개수로 초기화합니다.
word_cnt = len(words)

# words에 있는 단어 하나마다 반복해봅니다.
for word in words:
    # 현재 단어의 맨 앞 부분이 front_word에 있는 값들 중 하나로 시작하는 경우
    if word.startswith(front_word):
        # 현재 단어의 맨 앞에 있는 어포스트로피의 인덱스를 저장하는 변수를 선언합니다.
        apo_idx = word.index("\'")
        # 현재 단어의 어포스트로피 다음 알파벳을 저장하는 변수를 선언합니다.
        apo_next = word[apo_idx+1]

        # apo_next가 모음에 속한다면
        if apo_next in vowels:
            # 단어가 1개 더 있는 경우이므로 word_cnt에 1을 더해줍니다.
            word_cnt += 1

# 총 단어의 개수를 출력합니다.
print(word_cnt)