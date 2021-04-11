# https://www.acmicpc.net/problem/8949

# 두 정수 A, B를 공백을 두고 입력합니다.
# A, B는 1과 1,000,000 사이의 정수입니다.
A, B = input().split(' ')

A = A[::-1]
B = B[::-1]

if len(A) > len(B):
    short_num = B
    short_num_length = len(B)
else:
    short_num = A
    short_num_length = len(A)

result = ''

for index in range(short_num_length):
    result += str(int(A[index]) + int(B[index]))

result +=