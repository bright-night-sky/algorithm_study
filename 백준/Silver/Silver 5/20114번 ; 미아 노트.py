# https://www.acmicpc.net/problem/20114

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 첫째 줄에 원래 문자열의 길이 N, 세로로 번진 글자의 개수 H, 가로로 번진 글자의 개수 W를 공백으로 구분해 입력합니다.
# 1 <= N <= 100
# 1 <= H <= 10
# 1 <= W <= 10
# 각각 정수형으로 변환합니다.
N, H, W = map(int, stdin.readline().split(' '))
# 세로로 번진 것을 먼저 복원할 것이기 때문에 세로로 번진 것을 복원한 문자열을 저장할 변수를 선언합니다.
# 맨 끝의 \n은 떼어준 처음에 입력한 문자열로 초기화합니다.
height_restore_string = list(stdin.readline().rstrip())
# 가로로 번진 문자열의 길이를 저장하는 변수를 선언합니다.
spread_string_len = len(height_restore_string)
# 손상되기 전의 원래 문자열을 저장할 변수를 선언합니다.
restored_string = ''

# 위에서 번진 문자열을 이미 하나 입력했기 때문에
# 세로로 번진 글자의 개수 - 1만큼 반복합니다.
for _ in range(H - 1):
    # 번진 문자열을 입력합니다.
    # 맨 끝의 \n은 떼어줍니다.
    spread_string = stdin.readline().rstrip()

    # 번진 문자열의 길이만큼 반복합니다.
    for char_idx in range(spread_string_len):
        # 입력한 번진 문자열에서 현재의 글자가 ?가 아니라면
        if spread_string[char_idx] != '?':
            # 세로로 번진 것을 복원한 문자열의 현재 글자의 인덱스에 ?가 아닌 현재 글자로 변경해줍니다.
            height_restore_string[char_idx] = spread_string[char_idx]

# 번진 문자열의 길이에서 가로로 번진 글자의 개수 W만큼 건너뛰면서 반복합니다.
for char_idx in range(0, spread_string_len, W):
    # 현재 인덱스에서 가로로 번진 W만큼의 한 글자를 저장하는 변수를 선언합니다.
    char_set = height_restore_string[char_idx:char_idx+W]

    # char_set이 모두 ?로 이루어져 있다면
    if char_set == ['?'] * W:
        # restored_string에 ?를 넣어줍니다.
        restored_string += '?'
    # char_set에 한 글자라도 알파벳이 있다면
    else:
        # char_set에서 ?를 모두 빼줍니다.
        char_set = list(filter(lambda char: char != '?', char_set))
        # char_set에 있는 알파벳을 restored_string에 넣어줍니다.
        restored_string += char_set[0]

# 손상되기 전의 원래 문자열을 출력합니다.
print(restored_string)