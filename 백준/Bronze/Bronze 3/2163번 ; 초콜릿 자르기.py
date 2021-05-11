# https://www.acmicpc.net/problem/2163

# 두 정수 N, M 입력
# 1 <= N, M <= 300
N, M = map(int, input().split(' '))

# 2 X 2 -> 3번 쪼개야된다.
# 3 X 2 -> 5번 쪼개야된다.
# 4 X 2 -> 7번 쪼개야된다.
# 3 X 3 -> 8번 쪼개야된다.
# 결국 N X M - 1번 쪼개야된다.
print(N * M - 1)