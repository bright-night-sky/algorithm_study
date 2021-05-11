# https://www.acmicpc.net/problem/9093

# 첫째 줄에 테스트 케이스의 개수 T를 입력합니다.
T = int(input())

# 테스트 케이스의 개수 T만큼 반복합니다.
for i in range(T):
    # 문장 하나를 입력합니다.
    # 문장 안의 단어의 길이는 최대 20,
    # 문장의 길이는 최대 1000입니다.
    # 단어 사이사이에는 공백이 있습니다.
    sentence = input()
    # 입력한 문장을 공백으로 구분해 리스트 변수에 저장합니다.
    words = sentence.split(' ')
    # 문장에 각 단어들이 뒤집혀 있는 결과를 저장할 변수를 선언합니다.
    reverse_words = []

    # 문장에서 각 단어들을 반복해봅니다.
    for word in words:
        # 단어의 역순을 저장하는 변수를 선언합니다.
        reverse_word = word[::-1]
        # 뒤집혀 있는 단어를 reverse_words 리스트 변수에 넣어줍니다.
        reverse_words.append(reverse_word)

    # reverse_words의 단어들을 공백으로 구분해 출력해줍니다.
    print(' '.join(reverse_words))