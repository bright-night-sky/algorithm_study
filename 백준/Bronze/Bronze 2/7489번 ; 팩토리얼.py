# https://www.acmicpc.net/problem/7489

# 첫 줄에 테스트 케이스의 수 t를 입력합니다.
# 0 < t < 15
t = int(input())

# 테스트 케이스의 수만큼 반복합니다.
for i in range(t):
    # 정수 n을 입력합니다.
    # 0 < n < 1001
    n = int(input())

    result = 1

    for j in range(2, n+1):
        result = str(result * j).rstrip('0')