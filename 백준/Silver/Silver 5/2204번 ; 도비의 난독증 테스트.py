# https://www.acmicpc.net/problem/2204

# 0을 입력할 때까지 반복합니다.
while True:
    # 첫 줄에는 단어의 개수인 정수 n을 입력합니다.
    # 2 <= n <= 1000
    n = int(input())

    # 입력한 n이 0이라면
    if n == 0:
        # 반복문을 탈출하고 종료합니다.
        break
    # 입력한 n이 0이 아니라면
    else:
        # 입력할 단어들을 저장하는 리스트 변수를 선언합니다.
        words = []

        # 단어의 개수 n만큼 반복합니다.
        for word_index in range(n):
            # 단어를 하나 입력합니다.
            # 길이가 최대 20자입니다.
            word = input()

            # 입력한 단어를 words 리스트 변수에 넣어줍니다.
            words.append(word)

        # words 리스트 변수에 있는 단어들을 대소문자를 구분하지 않고 정렬을 해야하므로
        # 단어 하나하나를 소문자로 바꿨을 때의 사전 순을 기준으로 정렬합니다.
        words.sort(key=lambda word: word.lower())

        # words 리스트 변수의 맨 앞에 있는 단어를 출력합니다.
        print(words[0])