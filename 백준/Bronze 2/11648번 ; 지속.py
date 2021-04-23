# https://www.acmicpc.net/problem/11648

# 첫 번째 줄에는 선행하는 0이 없는 9자리 이하의 수를 하나 입력합니다.
num = input()

happy_phase = 0

multiple = 1

while True:
    if 0 <= multiple <= 9:
        print(happy_phase)
        break
    else:
        for i in num:
            multiple *= int(i)
            happy_phase += 1