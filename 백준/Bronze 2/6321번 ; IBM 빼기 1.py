# https://www.acmicpc.net/problem/6321

# 첫째 줄에 컴퓨터의 개수 n을 입력합니다.
n = int(input())

# 컴퓨터의 개수만큼 반복합니다.
for i in range(n):
    # 컴퓨터의 이름을 입력합니다.
    # 컴퓨터의 이름은 최대 50글자이며, 알파벳 대문자로만 이루어져 있습니다.
    computer = input()

    # 입력한 컴퓨터의 이름에서 각 글자를 알파벳 다음 순서로 저장할 변수를 선언합니다.
    next_computer = ''

    # 입력한 컴퓨터 이름에서 한 글자씩 반복합니다.
    for j in computer:
        # 현재 글자가 Z가 아니라면
        if j != 'Z':
            # 다음 알파벳을 next_computer에 넣어줍니다.
            next_computer += chr(ord(j) + 1)
        # 현재 글자가 Z라면
        else:
            # A를 next_computer에 넣어줍니다.
            next_computer += 'A'

    # 출력형식에 맞게 출력해줍니다.
    print(f"String #{i+1}")
    print(next_computer)
    print()