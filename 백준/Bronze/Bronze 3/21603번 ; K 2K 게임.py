# https://www.acmicpc.net/problem/21603

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 두 정수 N, K를 띄어쓰기를 사이에 두고 입력합니다.
# 1 <= N, K <= 10^5
# 각각 정수형으로 변환합니다.
N, K = map(int, stdin.readline().split(' '))
# K의 일의 자리 수인 f(K)를 저장하는 변수를 선언합니다.
fK = K % 10
# 2K의 일의 자리 수인 f(2K)를 저장하는 변수를 선언합니다.
f2K = (2 * K) % 10
# 문제의 조건을 만족하는 x들을 저장할 리스트 변수를 선언합니다.
f = []

# 1부터 N까지 반복합니다.
for x in range(1, N+1):
    # 자연수 x의 일의 자리 수인 f(x)를 저장하는 변수를 선언합니다.
    fx = x % 10

    # 현재 숫자가 문제의 조건인 f(x) != f(K), f(x) != f(2K)를 만족하면
    if fx != fK and fx != f2K:
        # x를 문자열로 변환하고 f에 넣어줍니다.
        f.append(str(x))

# 조건을 만족하는 개수인 f의 길이를 출력합니다.
print(len(f))
# f의 값들을 공백을 사이에 두고 출력합니다.
print(' '.join(f))