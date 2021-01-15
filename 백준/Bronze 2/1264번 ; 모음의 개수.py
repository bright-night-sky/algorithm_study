# https://www.acmicpc.net/problem/1264

# 모음 리스트
vowels = ['a', 'e', 'i', 'o', 'u']

# 한 문장에서 모음의 갯수를 저장할 변수
vowel_count = 0

# #을 입력할 때까지 영어 한 문장 입력
while True:
    # 영어 한 문장이나 # 입력
    # 각 줄은 최대 255글자이다.
    string = input()

    # #을 입력하면
    if string == '#':
        # 반복문 탈출
        break

    # 모음 리스트의 각 모음들을 돌려가면서 찾는다.
    for vowel in vowels:
        # 영어 한 문장의 모음의 대소문자 구별없이 갯수를 세어 모음의 갯수 변수에 더한다.
        vowel_count += string.count(vowel) + string.count(vowel.upper())

    # 영어 한 문장마다 모음의 갯수를 출력한다.
    print(vowel_count)
    # 모음의 갯수는 0으로 초기화한다.
    vowel_count = 0