# https://www.acmicpc.net/problem/14563

# 첫째 줄에 자연수의 개수 T를 입력합니다.
# T는 1000보다 작은 수입니다.
T = int(input())

Ns = list(map(int, input().split(' ')))

for N in Ns:
    proper_divisor = [1]

    for num in range(2, N // 2 + 1):
        if N % num == 0:
            proper_divisor.append(num)

    proper_divisor_sum = sum(proper_divisor)

    if proper_divisor_sum == N:
        print("Perfect")
    elif proper_divisor_sum < N:
        print("Deficient")
    elif proper_divisor_sum > N:
        print("Abundant")