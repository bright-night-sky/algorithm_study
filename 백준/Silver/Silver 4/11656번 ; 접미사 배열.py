# https://www.acmicpc.net/problem/11656

# readline을 사용하기 위해 import합니다.
from sys import stdin

# 첫째 줄에 문자열 S를 입력합니다.
# 알파벳 소문자로만 이루어져 있고, 길이는 1,000보다 작거나 같습니다.
# 맨 끝의 \n은 떼어줍니다.
S = stdin.readline().rstrip()
# 문자열 S의 길이를 저장하는 변수를 선언합니다.
S_len = len(S)
# 문자열 S의 모든 접미사들을 저장할 리스트 변수를 선언합니다.
suffixes = []

# 문자열 S의 길이만큼 반복합니다.
for start_idx in range(S_len):
    # 문자열 S의 현재 start_idx에서 끝 글자까지의 한 접미사를 구하고 suffixes에 넣어줍니다.
    suffixes.append(S[start_idx:])

# suffixes에 있는 접미사들을 사전순으로 정렬합니다.
suffixes.sort()

# 출력 형식에 맞게 하나씩 출력합니다.
for suffix in suffixes:
    print(suffix)