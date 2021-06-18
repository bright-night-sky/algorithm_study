# https://www.acmicpc.net/problem/10539

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 첫째 줄에는 수열 B의 길이 N을 입력합니다.
# 1 <= N <= 100
# 정수형으로 변환합니다.
N = int(stdin.readline())
# 둘째 줄에는 수열 Bi를 이루는 N개의 정수를 공백으로 구분해 입력합니다.
# 1 <= Bi <= 10^9
# 각각 정수형으로 변환하고 리스트 변수에 넣어줍니다.
B = list(map(int, stdin.readline().split(' ')))
# 길이가 N인 수열 A를 리스트 변수로 선언합니다.
# 모든 값을 0으로 초기화합니다.
A = [0] * N

# 수열의 길이 N만큼 반복합니다.
for idx in range(N):
    # Ai의 값을 저장하는 변수를 선언합니다.
    # (수열 B에서 현재 인덱스의 값) X (현재 인덱스 + 1) - (수열 A의 첫 번째부터 현재 인덱스+1까지의 합)
    Ai = B[idx] * (idx + 1) - sum(A[:idx+1])
    # 수열 A의 현재 인덱스에 Ai의 값을 초기화합니다.
    A[idx] = Ai

# 출력 형식에 맞게 Ai들을 출력합니다.
for Ai in A:
    print(Ai, end=' ')