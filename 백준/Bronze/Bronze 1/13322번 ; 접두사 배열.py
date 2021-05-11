# https://www.acmicpc.net/problem/13322

# 첫 줄에 알파벳 소문자로 이루어진 문자열 S를 입력합니다.
# 문자열 S의 길이는 1 이상 100000 이하입니다.
S = input()

suffix_array = []

for index in range(len(S)):
    suffix = S[index:len(S)]
    suffix_array.append(suffix)

dictionary_suffix_array = sorted(suffix_array)

for sorted_suffix in dictionary_suffix_array:
    print(suffix_array.index(sorted_suffix))
