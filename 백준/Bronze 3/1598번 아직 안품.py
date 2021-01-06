# https://www.acmicpc.net/problem/1598

num1, num2 = map(int, input().split(' '))

height_distance = abs((num1 % 4) - (num2 % 4))
width_distance = abs(num1 - num2) // 4 + 1