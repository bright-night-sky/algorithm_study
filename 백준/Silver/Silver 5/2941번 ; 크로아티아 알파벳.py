# https://www.acmicpc.net/problem/2941

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 첫째 줄에 최대 100글자의 크로아티아 단어를 입력합니다.
# 알파벳 소문자, '-', '='로만 이루어져 있습니다.
# 맨 끝의 \n은 떼어줍니다.
croatian_word = stdin.readline().rstrip()
# 특이한 크로아티아 알파벳을 저장하는 튜플 변수를 선언합니다.
croatian_alphabet = ('c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=')
# 입력한 크로아티아 단어의 길이를 저장하는 변수를 선언합니다.
word_length = len(croatian_word)
# 크로아티아 알파벳의 개수를 저장하는 변수를 선언합니다.
# 0으로 초기화합니다.
alphabet_cnt = 0

# 크로아티아 단어 한 글자씩 읽을 인덱스를 저장하는 변수를 선언합니다.
# 0으로 초기화합니다.
idx = 0
# 크로아티아 단어를 한 글자씩 반복해봅니다.
while idx < word_length:
    # 현재 인덱스의 글자와 다음 글자를 저장하는 변수를 선언합니다.
    two_alphabet_bundle = croatian_word[idx:idx+2]
    # 현재 인덱스와 다음 다음 글자까지 저장하는 변수를 선언합니다.
    three_alphabet_bundle = croatian_word[idx:idx+3]

    # two_alphabet_bundle이 특이한 크로아티아 알파벳에 속한다면
    if two_alphabet_bundle in croatian_alphabet:
        # 크로아티아 알파벳 개수에 1을 더해줍니다.
        alphabet_cnt += 1
        # 인덱스에 2를 더해줍니다.
        idx += 2
    # three_alphabet_bundle이 특이한 크로아티아 알파벳에 속한다면
    elif three_alphabet_bundle in croatian_alphabet:
        # 크로아티아 알파벳 개수에 1을 더해줍니다.
        alphabet_cnt += 1
        # 인덱스에 3을 더해줍니다.
        idx += 3
    # 그 외의 경우에는
    else:
        # 크로아티아 알파벳 개수에 1을 더해줍니다.
        alphabet_cnt += 1
        # 현재 인덱스의 한 글자가 알파벳이므로 인덱스에 1을 더해줍니다.
        idx += 1

# 크로아티아 알파벳의 개수를 출력합니다.
print(alphabet_cnt)