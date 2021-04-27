# https://www.acmicpc.net/problem/1919

# 첫째 줄에 영어 단어 소문자를 입력합니다.
word1 = list(input())

word2 = list(input())

for alphabet in word1:
    if alphabet in word2:
        word1.remove(alphabet)
        word2.remove(alphabet)

for alphabet in word2:
    if alphabet in word1:
        word1.remove(alphabet)
        word2.remove(alphabet)

print(len(word1) + len(word2))