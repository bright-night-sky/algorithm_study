# https://www.acmicpc.net/problem/1085
from math import sqrt

x, y, w, h = map(int, input().split(' '))

zero_to_x = x
zero_to_y = y
x_to_w = w-x
y_to_h = h-y
min_distance = min(zero_to_x, zero_to_y, x_to_w, y_to_h)
print(min_distance)
