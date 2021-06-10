# https://www.acmicpc.net/problem/3054

# readline을 사용하기 위해 import합니다.
from sys import stdin

# 첫째 줄에 알파벳 대문자로 이루어진 최대 15글자 단어를 입력합니다.
word = stdin.readline().rstrip()
# 입력한 단어의 길이를 저장하는 변수를 선언합니다.
word_len = len(word)
# 프레임들로 장식한 결과의 각 줄들을 저장하는 리스트 변수를 선언합니다.
# 각 줄의 첫 문자들로 초기화합니다.
lines = ['.', '.', '#', '.', '.']

# 입력한 단어에서의 문자의 개수만큼 반복합니다.
for char_idx in range(word_len):
    # 현재 문자의 위치가 3의 배수가 아니라면
    if (char_idx + 1) % 3 != 0:
        # 피터팬 프레임에서 가운데 세 개의 열 모야을 lines의 각 줄에 넣어줍니다.
        # .#.
        # #.#
        # .X.
        # #.#
        # .#.
        lines[0] += '.#.'
        lines[1] += '#.#'
        lines[2] += f'.{word[char_idx]}.'
        lines[3] += '#.#'
        lines[4] += '.#.'
    # 현재 문자의 위치가 3의 배수라면
    else:
        # 현재 문자를 웬디 프레임으로 장식해 각 줄에 넣어줍니다.
        lines[0] += '..*..'
        lines[1] += '.*.*.'
        lines[2] += f'*.{word[char_idx]}.*'
        lines[3] += '.*.*.'
        lines[4] += '..*..'

    # 현재 문자의 장식이 피터팬 프레임으로 장식되었는데
    # 다음 문자의 장식도 피터팬 프레임으로 장식될 때의 처리입니다.
    # 현재 문자의 위치를 3으로 나누었을 때 나머지가 1이라면
    if (char_idx + 1) % 3 == 1:
        # 각 줄에 피터팬 프레임의 첫 번째 열 모양을 넣어줍니다.
        lines[0] += '.'
        lines[1] += '.'
        lines[2] += '#'
        lines[3] += '.'
        lines[4] += '.'

# 마지막 문자가 웬디 프레임으로 장식될 문자 위치의 바로 뒤 문자일 때의 처리입니다.
# 단어의 길이를 3으로 나누었을 때 나머지가 2라면
if word_len % 3 == 2:
    # 각 줄에 피터팬 프레임의 첫 번째 열 모양을 넣어줍니다.
    lines[0] += '.'
    lines[1] += '.'
    lines[2] += '#'
    lines[3] += '.'
    lines[4] += '.'

# lines에 저장되어 있는 각 줄들의 모양을 출력합니다.
for line in lines:
    print(line)
