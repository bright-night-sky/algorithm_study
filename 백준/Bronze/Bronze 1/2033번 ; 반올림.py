# https://www.acmicpc.net/problem/2033

# 첫째 줄에 정수 N을 입력합니다.
# 0 <= N <= 99,999,999
N = input()

N_length = len(N)

# for position in range(1, N_length):
#     N = round(int(N), -position)

print(round(float(N), 0))