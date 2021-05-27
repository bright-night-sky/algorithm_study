# https://www.acmicpc.net/problem/14405

# readline을 사용하기 위해 import합니다.
from sys import stdin

# 첫째 줄에 문자열 S를 입력합니다.
# 알파벳 소문자로만 이루어진 문자열이며, 길이는 5000을 넘지 않습니다.
S = stdin.readline().rstrip()
# 피카츄의 pi, ka, chu 음절들을 저장하는 리스트 변수를 선언합니다.
pikachu = ['pi', 'ka', 'chu']

# pi, ka, chu 음절 하나씩 반복해봅니다.
for syllable in pikachu:
    # 문자열 S에서 pi, ka, chu 음절들을 공백 하나로 변경합니다.
    S = S.replace(syllable, ' ')

# 변경된 문자열 S에서 한 글자씩 반복합니다.
for character in S:
    # 현재 글자가 알파벳 a부터 z에 속한다면
    if ord('a') <= ord(character) <= ord('z'):
        # NO를 출력합니다.
        print('NO')
        # 반복문을 탈출합니다.
        break
# 반복문을 중간에 탈출하지 않고 끝까지 끝낸다면
else:
    # YES를 출력합니다.
    print('YES')
