# https://www.acmicpc.net/problem/11945

# 첫째 줄에는 두 개의 정수 N, M을 입력합니다.
# 0 <= N, M <= 10
N, M = map(int, input().split(' '))

# 붕어빵의 모양을 저장할 변수를 선언합니다.
carp_bread = []

# 둘째 줄부터 N개의 줄에 걸쳐 붕어빵의 모양을 입력합니다.
for i in range(N):
    # 한 줄마다 붕어빵의 모양을 차례로 입력합니다.
    carp_bread.append(input())

# 붕어빵이 좌우로 뒤집힌 모양을 출력합니다.
for row in carp_bread:
    print(row[::-1])