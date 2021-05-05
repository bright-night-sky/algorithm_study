# https://www.acmicpc.net/problem/16171

# 첫 번째 줄에는 알파벳 대소문자, 숫자로 이루어진 문자열 S를 입력합니다.
# 1 <= |S| <= 100
S = input()

# 두 번째 줄에는 성민이가 찾고자 하는 알파벳 대소문자로만 이루어진 문자열 K를 입력합니다.
# 1 <= |K| <= 100
K = input()

# 문자열 S에서 숫자를 빼고 난 뒤의 문자열을 저장하는 변수를 선언합니다.
non_num_string = ''

# 문자열 S에서 한 글자씩 반복합니다.
for character in S:
    # 현재 글자가 a ~ z, A ~ Z에 속하면
    if ord('a') <= ord(character) <= ord('z') or ord('A') <= ord(character) <= ord('Z'):
        # non_num_string에 현재 글자를 넣어줍니다.
        non_num_string += character

# non_num_string에 K가 들어있다면
if non_num_string.find(K) != -1:
    # 1을 출력합니다.
    print(1)
# non_num_string에 K가 들어있지 않다면
else:
    # 0을 출력합니다.
    print(0)