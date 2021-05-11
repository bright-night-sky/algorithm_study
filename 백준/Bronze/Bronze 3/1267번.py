# https://www.acmicpc.net/problem/1267

N = int(input())
calltimes = list(map(int, input().split(' ')))
youngsik = 0
minsik = 0

for i in calltimes:
    youngsik = youngsik + (i // 30 * 10) + 10
    minsik = minsik + (i // 60 * 15) + 15

if youngsik > minsik:
    print('M', minsik)
elif youngsik < minsik:
    print('Y', youngsik)
else:
    print('Y', 'M', youngsik)