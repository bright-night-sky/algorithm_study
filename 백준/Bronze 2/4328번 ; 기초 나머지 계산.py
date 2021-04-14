# https://www.acmicpc.net/problem/4328

while True:
    nums = input()

    if nums == '0':
        break

    b, p, m = nums.split(' ')
    p = int(p, int(b))
    m = int(m, int(b))

    remainder = p % m
    result = ''

