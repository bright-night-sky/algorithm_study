# https://www.acmicpc.net/problem/2588

# (1), (2)의 세 자리 자연수 입력
one = input()
two = input()

# (3)에 들어갈 숫자 계산 및 출력
three = int(one) * int(two[2])
print(three)

# (4)에 들어갈 숫자 계산 및 출력
four = int(one) * int(two[1])
print(four)

# (5)에 들어갈 숫자 계산 및 출력
five = int(one) * int(two[0])
print(five)

# (6)에 들어갈 숫자 : 그냥 계산 결과 및 출력
six = int(one) * int(two)
print(six)

