# https://www.acmicpc.net/problem/11383

# 첫 번째 줄에 N, M을 입력합니다.
# 1 <= N, M <= 10
N, M = map(int, input().split(' '))

# M개의 문자로 주어지는 첫 번째 이미지를 뜻하는 한 줄을 저장하는 리스트 변수를 선언합니다.
origin_words = []
# 2M개의 문자로 주어지는 두 번째 이미지를 뜻하는 한 줄을 저장하는 리스트 변수를 선언합니다.
twice_or_not_words = []

# 결과를 저장하는 변수를 선언합니다.
# 첫 번째 이미지를 늘려 두 번째 이미지가 되지 않는 경우를 판단할 것이기 때문에
# Eyfa로 초기화해줍니다.
result = "Eyfa"

# N개의 줄만큼 반복해봅니다.
for i in range(N):
    # 길이가 M인 문자 한 줄을 입력합니다.
    # 영문 알파벳 대, 소문자로만 입력합니다.
    word = input()

    # 입력한 한 줄의 단어를 origin_words에 넣어줍니다.
    origin_words.append(word)

# N개의 줄만큼 반복해봅니다.
for i in range(N):
    # 길이가 2M인 문자 한 줄을 입력합니다.
    # 영문 알파벳 대, 소문자로만 입력합니다.
    word = input()

    # 입력한 한 줄의 단어를 twice_or_not_words에 넣어줍니다.
    twice_or_not_words.append(word)

# M개의 길이인 첫 번째 이미지를 뜻하는 단어들과
# 2M개의 길이인 두 번째 이미지를 뜻하는 단어들이 각각 N개만큼 있으므로
# N개만큼 반복해봅니다.
for index in range(N):
    # origin_words에서 한 단어를 2배로 늘릴 때 그 2배로 늘린 단어를 저장하는 변수를 선언합니다.
    twice_origin_word = ''

    # origin_words에서 뽑은 현재의 단어에서 한 알파벳씩 반복해봅니다.
    for alphabet in origin_words[index]:
        # 현재의 알파벳 2개를 twice_origin_word에 넣어줍니다.
        twice_origin_word += alphabet * 2

    # 원래 단어를 2배로 늘린 것과 입력한 2배 단어가 같지 않다면
    if twice_origin_word != twice_or_not_words[index]:
        # 결과 변수에 Not Eyfa를 저장합니다.
        result = "Not Eyfa"
        # 첫 번째로 주어진 이미지를 가로로 두 배로 늘렸을 때
        # 두 번째 이미지가 되지 않는 경우가 하나라도 생겼으므로
        # 반복문을 탈출합니다.
        break

# 결과를 출력합니다.
print(result)