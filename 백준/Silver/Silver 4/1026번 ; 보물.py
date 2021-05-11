# https://www.acmicpc.net/problem/1026

# 문제의 함수 S를 구현합니다.
# 리스트 A, B와 A, B의 똑같은 길이인 N을 매개변수로 받습니다.
def S(A, B, N):
    # S의 결과인 합을 저장할 변수를 선언합니다.
    sum_result = 0

    # 리스트 A, B의 길이인 N만큼 반복합니다.
    for index in range(N):
        # sum_result에 A와 B의 현재 인덱스의 숫자를 곱한 것을 더합니다.
        sum_result += A[index] * B[index]

    # sum_result의 값을 반환합니다.
    return sum_result

# 첫째 줄에 N을 입력합니다.
# 50보다 작거나 같은 자연수입니다.
N = int(input())

# 둘째 줄에 N개의 수를 공백으로 구분해 입력합니다.
# 각 숫자는 정수형으로 변환하고 리스트 변수 A에 넣어줍니다.
A = list(map(int, input().split(' ')))
# 셋째 줄에 N개의 수를 공백으로 구분해 입력합니다.
# 각 숫자는 정수형으로 변환하고 리스트 변수 B에 넣어줍니다.
B = list(map(int, input().split(' ')))

# S의 최솟값을 구하기 위해서는 A의 숫자 중 작은 순서대로, B의 숫자 중 큰 순서대로 곱한 것을 더하면 됩니다.
# 혹은 A의 숫자 중 큰 순서대로, B의 숫자 중 작은 순서대로 곱한 것을 더하면 됩니다.

# A는 오름차순으로 정렬해줍니다.
A = sorted(A)
# B는 내림차순으로 정렬해줍니다.
B = sorted(B, reverse=True)

# 리스트 변수 A, B, 첫 번째로 입력한 N의 값을 함수 S에 넣어주고
# 반환된 값을 출력합니다.
print(S(A, B, N))