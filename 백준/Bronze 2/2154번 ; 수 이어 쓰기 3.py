# https://www.acmicpc.net/problem/2154

# 첫째 줄에 N을 입력합니다.
# 1 <= N <= 100,000
N = input()

N_length = len(N)

N_string = ''
for i in range(1, int(N)+1):
    N_string += str(i)

N_string_length = len(N_string)

for index in range(0, N_string_length):
    if N == N_string[index:index+N_length]:
        print(index+1)
        break