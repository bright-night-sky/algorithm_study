# https://www.acmicpc.net/problem/1032

# readline을 사용하기 위해 import합니다.
from sys import stdin

# 첫째 줄에 파일 이름의 개수 N을 입력합니다.
# N은 50보다 작거나 같은 자연수입니다.
N = int(stdin.readline().rstrip())

# 파일 이름들을 저장하는 리스트 변수를 선언합니다.
filenames = []

# 파일 이름의 개수 N만큼 반복합니다.
for file_idx in range(N):
    # 파일 이름 하나를 입력합니다.
    # 파일 이름의 길이는 모두 같고 길이는 최대 50입니다.
    # 파일 이름은 알파벳과 "." 그리고 "?"로만 이루어져 있습니다.
    filename = stdin.readline().rstrip()
    # 입력한 파일 이름을 filenames에 넣어줍니다.
    filenames.append(filename)

# 패턴을 저장하는 변수를 선언합니다.
# 맨 처음에 입력한 파일 이름을 리스트 형태로 초기화해줍니다.
pattern = list(filenames[0])
# 파일 이름들의 길이는 모두 같으므로 패턴의 길이를 첫 파일 이름의 길이로 초기화해줍니다.
pattern_len = len(pattern)

# 패턴과 파일 이름들을 하나씩 비교해봅니다.
# 파일 이름들을 하나씩 반복해봅니다.
for filename in filenames:
    # 패턴과 파일 이름에서 같은 위치에 있는 글자를 반복해봅니다.
    for name_idx in range(pattern_len):
        # 패턴과 파일 이름의 같은 위치에 있는 글자가 다르다면
        if pattern[name_idx] != filename[name_idx]:
            # 패턴의 현재 위치에 있는 글자를 ?로 바꿔줍니다.
            pattern[name_idx] = "?"

# 패턴을 출력 형식에 맞게 출력합니다.
print("".join(pattern))