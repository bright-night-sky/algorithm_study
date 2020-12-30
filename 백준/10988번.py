# https://www.acmicpc.net/problem/10988

string = input()

if string == string[::-1]:
    print(1)
else:
    print(0)