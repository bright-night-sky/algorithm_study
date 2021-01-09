# https://www.acmicpc.net/problem/19698

# N, W, H, L 입력
N, W, H, L = map(int, input().split(' '))

# 수평 길이의 개수
width_count = W // L
# 수직 길이의 개수
height_count = H // L

# 위의 두 개수를 곱하면 소들이 입주할 수 있는 최대 방의 개수이다.
print(width_count * height_count)