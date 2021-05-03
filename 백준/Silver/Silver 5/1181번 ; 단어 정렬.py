# https://www.acmicpc.net/problem/1181

# 첫째 줄에 단어의 개수 N을 입력합니다.
# 1 <= N <= 20,000
N = int(input())

# 중복된 단어는 하나만 있어야 하므로 단어들을 저장하는 세트 변수를 선언합니다.
words = set()

# 단어의 개수 N만큼 반복합니다.
for word_index in range(N):
    # 단어를 하나 입력합니다.
    # 단어의 길이는 50을 넘지 않습니다.
    word = input()

    # 입력한 단어를 words 세트 변수에 넣어줍니다.
    words.add(word)

# words 세트 변수를 리스트 변수로 바꿔줍니다.
words = list(words)
# words 리스트 변수 내부의 값들을
# 길이가 짧은 것부터
# 길이가 같다면 사전 순으로 정렬해줍니다.
words.sort(key=lambda word: (len(word), word))

# words 리스트 변수 내부의 단어들을 하나씩 출력해줍니다.
for word in words:
    print(word)