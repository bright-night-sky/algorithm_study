# https://www.acmicpc.net/problem/1032

# 첫째 줄에 파일 이름의 개수 N을 입력합니다.
N = int(input())

file_names = []

for file_index in range(N):
    file_name = input()

    file_names.append(file_name)

file_name_length = len(file_names[0])

