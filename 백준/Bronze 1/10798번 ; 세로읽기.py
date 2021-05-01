# https://www.acmicpc.net/problem/10798

# 입력한 문자열들을 저장하는 리스트 변수를 선언합니다.
strings = []

# 입력한 문자열 중 가장 긴 길이를 저장하는 변수를 선언합니다.
max_string_length = 0

# 5번 반복합니다.
for string_index in range(5):
    # 문자열을 하나 입력합니다.
    string = input()

    # strings에 입력한 문자열을 넣어줍니다.
    strings.append(string)

    # 이전까지 최대 문자열 길이보다 현재 입력한 문자열의 길이가 더 길다면
    if len(string) >= max_string_length:
        # 최대 문자열 길이 변수에 현재 문자열 길이를 저장합니다.
        max_string_length = len(string)

# 세로로 읽은 결과를 저장하는 변수를 선언합니다.
column_string = ''

# 최대 문자열 길이만큼 반복합니다.
for index in range(max_string_length):
    # 문자열 하나마다 반복합니다.
    for string in strings:
        # 현재 문자열에서 현재 읽을 인덱스가 없다면
        if len(string) < index + 1:
            # 그냥 넘어갑니다.
            continue
        # 현재 문자열에서 현재 읽을 인덱스가 있다면
        else:
            # column_string에 현재 문자열의 현재 인덱스의 문자를 넣어줍니다.
            column_string += string[index]

# 세로로 읽은 결과를 출력합니다.
print(column_string)