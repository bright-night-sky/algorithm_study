# https://www.acmicpc.net/problem/5554

time_sum = 0

for i in range(0, 4):
    sec = int(input())
    time_sum += sec

print(time_sum // 60)
print(time_sum % 60)