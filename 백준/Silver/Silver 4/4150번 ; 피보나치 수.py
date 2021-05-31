# https://www.acmicpc.net/problem/4150

from sys import stdin

fibo_num = [1, 1]

def fibo(n):
    if n == 1:
        return fibo_num[0]
    elif n == 2:
        return fibo_num[1]
    else:
        fibo_num.append(fibo(n - 1) + fibo(n - 2))
        return fibo_num[n - 1]

n = int(stdin.readline())

print(fibo(n))