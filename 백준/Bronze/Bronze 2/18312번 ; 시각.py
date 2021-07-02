# https://www.acmicpc.net/problem/18312

from sys import stdin


N, K = map(int, stdin.readline().split(' '))
end_time = N * 3600 + 59 * 60 + 59
K_cnt = 0

for sec_time in range(end_time + 1):
    time_string = ''

    hour = sec_time // 3600
    sec_time -= hour * 3600
    time_string += str(hour)

    minute = sec_time // 60
    sec_time -= minute * 60
    time_string += str(minute)

    time_string += str(sec_time)

    if str(K) in time_string:
        K_cnt += 1

print(K_cnt)