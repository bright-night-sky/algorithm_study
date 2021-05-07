# https://www.acmicpc.net/problem/2408

# 수의 개수 N을 입력합니다.
# 1 <= N <= 10
N = int(input())

equation = ''

for num_or_operator_index in range(N):
    num_or_operator = input()

    equation += num_or_operator

print(eval(equation))