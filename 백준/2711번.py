# https://www.acmicpc.net/problem/2711

test_case = int(input())

for i in range(0, test_case):
    mis_index, string = input().split(' ')
    mis_index = int(mis_index) - 1
    pre_str = string[0:mis_index]
    suf_str = string[mis_index+1:]
    string = pre_str + suf_str
    print(string)
