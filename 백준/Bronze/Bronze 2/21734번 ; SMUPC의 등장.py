# https://www.acmicpc.net/problem/21734

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 첫 줄에 알파벳 소문자로만 이루어진 단어 S를 입력합니다.
# 길이는 10을 넘지 않습니다.
# 맨 끝의 \n을 떼어줍니다.
S = stdin.readline().rstrip()

# S의 한 글자씩 반복합니다.
for char in S:
    # 현재 글자의 10진법 아스키코드 값을 저장하는 변수를 선언합니다.
    char_ascii = ord(char)
    # 아스키코드 값의 각 자릿수의 합을 저장하는 변수를 선언합니다.
    position_sum = sum(map(int, list(str(char_ascii))))

    # 현재 글자를 position_num만큼 반복해서 출력합니다.
    print(char * position_sum)