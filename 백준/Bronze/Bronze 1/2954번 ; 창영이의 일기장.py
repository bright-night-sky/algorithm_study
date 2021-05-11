# https://www.acmicpc.net/problem/2954

# 첫째 줄에 알파벳 소문자, 공백으로만 이루어진 문장을 입력합니다.
# 모든 단어는 공백 하나로 구분되어져 있습니다.
# 문장의 길이는 최대 100입니다.
diary = input()

vowels = ['a', 'e', 'i', 'o', 'u']

origin = ''

diary_length = len(diary)

for index in range(diary_length):
    if diary[index] in vowels and diary[index:index+2] == (diary[index] + 'p' + diary[index]):
