# https://www.acmicpc.net/problem/19843

# 첫 줄에는 일주일에 자야할 시간을 나타내는 정수 T, 민티가 평일 동안 잠든 횟수를 나타내는 정수 N을 입력합니다.
# 0 <= T <= 168
# 0 <= N <= 10
T, N = map(int, input().split(' '))

total_sleeping_time = 0

for i in range(N):
    sleep = list(input().split(' '))

    if sleep[0] == sleep[2]:
        total_sleeping_time += int(sleep[3]) - int(sleep[1])
    else:
        total_sleeping_time += int(sleep[3]) + 24 - int(sleep[1])

if total_sleeping_time >= T:
    print(0)
elif T - total_sleeping_time <= 48:
    print(T - total_sleeping_time)
else:
    print(-1)