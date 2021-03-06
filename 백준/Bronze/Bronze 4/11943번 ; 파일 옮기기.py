# https://www.acmicpc.net/problem/11943

# 첫 번째 줄에는 첫 번째 바구니에 있는 사과와 오렌지의 수 A, B를 입력
# 0 <= A, B <= 1,000
A, B = map(int, input().split(' '))

# 두 번째 줄에는 두 번째 바구니에 있는 사과와 오렌지의 수 C, D를 입력
# 0 <= C, D <= 1,000
C, D = map(int, input().split(' '))

# 첫 번째 바구니에서 두 번째 바구니로 사과를 옮기는 횟수와 두 번째 바구니에서 첫 번째 바구니로 오렌지를 옮기는 횟수를 더한 값을 저장
AD_move = A + D

# 두 번째 바구니에서 첫 번째 바구니로 사과를 옮기는 횟수와 첫 번째 바구니에서 두 번째 바구니로 오렌지를 옮기는 횟수를 더한 값을 저장
BC_move = B + C

# 위의 2개의 값 중 더 작은 값이 사과와 오렌지를 옮기는 최소 횟수이다.
print(min(AD_move, BC_move))