# https://www.acmicpc.net/problem/17608

# 첫 번째 줄에는 막대기의 개수를 나타내는 정수 N을 입력합니다.
# 2 <= N <= 100,000
N = int(input())

sticks = []

for stick_index in range(N):
    stick = int(input())

    sticks.append(stick)

seen_sticks_count = 0
last_right_stick = sticks[-1]

for stick in sticks:
    if stick > last_right_stick:
        seen_sticks_count += 1

print(seen_sticks_count + 1)