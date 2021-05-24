# https://www.acmicpc.net/problem/4388

from sys import stdin

while True:
    num1, num2 = stdin.readline().rstrip().split(' ')

    if num1 == num2 == '0':
        break

    carry_cnt = 0
    num1_length = len(num1)
    num2_length = len(num2)
    short_length = min(num1_length, num2_length)
    long_length_num = None
    if num1_length > num2_length:
        long_length_num = num1
    else:
        long_length_num = num2
    carry = 0
    for idx in range(-1, -short_length-1, -1):
        if int(num1[idx]) + int(num2[idx]) + carry >= 10:
            carry = 1
            carry_cnt += 1
        else:
            carry = 0

    if long_length_num[-short_length-1] == '9' and carry == 1:
        print(long_length_num[-short_length-2])
        carry_cnt += 1

    print(carry_cnt)