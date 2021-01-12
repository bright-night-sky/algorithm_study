# https://www.acmicpc.net/problem/2052

# 자연수 N 입력
# 1 <= N <= 250
N = int(input())

# 2의 -N승 출력
print('{0:.1000f}'.format(1 / 2 ** N))
print("%g" % (1 / 2 ** N))
print(float(1 / 2 ** N))