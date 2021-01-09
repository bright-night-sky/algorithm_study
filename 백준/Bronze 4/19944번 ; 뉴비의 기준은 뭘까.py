# https://www.acmicpc.net/problem/19944

# N, M 입력
# 3 <= N <= 1,000
# 1 <= M <= 1,000
N, M = map(int, input().split(' '))

# M학년이 1학년, 2학년이면 뉴비이다.
if M == 1 or M == 2:
    # NEWBIE! 출력
    print("NEWBIE!")
# M학년이 1학년, 2학년(뉴비)이 아니면서, N학년 이하이면 올드비이다.
elif M > 2 and M <= N:
    # OLDBIE! 출력
    print("OLDBIE!")
# 뉴비도 올드비도 아니면 TLE이다.
else:
    # TLE! 출력
    print("TLE!")
