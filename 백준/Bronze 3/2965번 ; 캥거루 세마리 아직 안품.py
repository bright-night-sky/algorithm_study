# https://www.acmicpc.net/problem/2965

# 첫째 줄에 세 캥거루의 초기 위치 A, B, C를 입력합니다.
# 0 < A < B < C < 100
A, B, C = map(int, input().split(' '))

# 캥거루가 최대로 움직이려면
# 바깥에 있는 두 캥거루와 중간에 있는 캥거루와의 거리를 각각 재어보고,
# 더 짧은 거리를 가진 캥거루가 더 긴 거리의 중간에 점프하는 식으로 계속 재어보면
# 최대 점프 수가 나온다.

# 점프 수를 저장하는 변수입니다.
jump = 0

# 가장 작은 정수에 위치한 캥거루를 저장하는 변수입니다.
small = A
# 중간 정수에 위치한 캥거루를 저장하는 변수입니다.
mid = B
# 가장 큰 정수에 위치한 캥거루를 저장하는 변수입니다.
big = C

# 가장 작은 정수와 중간의 차이를 계산해서 저장하는 변수입니다.
small_to_mid = abs(small - mid)
# 가장 큰 정수와 중간의 차이를 계산해서 저장하는 변수입니다.
big_to_mid = abs(big - mid)

while True:
    if small_to_mid == 1 and big_to_mid == 1:
        break

    # 가장 작은 정수와 중간의 차이가 더 크다면
    if small_to_mid > big_to_mid:
        # mid의 값이 변하므로 임시 변수로 값을 저장해둡니다.
        temp = mid
        # 가장 큰 정수에 위치한 캥거루가 그 차이의 중간으로 점프합니다.
        mid = (mid - small) / 2
        # 그리고 크기의 순서에 맞게 변수에 저장합니다.
        big = temp
        # 캥거루가 점프를 한 번 했으므로 점프수에 1을 더해줍니다.
        jump += 1