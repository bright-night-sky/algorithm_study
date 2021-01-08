# https://www.acmicpc.net/problem/1159

# 선수의 수 N 입력
# 1 <= N <= 150
N = int(input())

# 성의 첫 글자를 알파벳 순서대로 순회하면서 찾아가기 위해 필요한 알파벳 나열 변수
alphabets = 'abcdefghijklmnopqrstuvwxyz'

# 선수들의 성을 저장할 리스트 변수
player = []

# 알파벳 별로 선수들의 성의 개수를 저장하는 변수
count = 0

# 성의 첫 글자가 5명 이상인 경우 그 성의 첫 글자를 저장하는 리스트 변수
first_names = []

# 선수의 수만큼 선수들의 성 입력
for i in range(0, N):
    # 입력한 선수들의 성을 player 리스트 변수에 삽입
    first_name = player.append(input())

# a ~ z 순회하면서 선수의 성의 첫 글자가 해당 알파벳이랑 똑같은지 세어본다.
for alphabet in alphabets:
    for i in player:
        if alphabet == i[0]:
            count += 1

            # 만약 성의 첫 글자가 똑같은 선수가 5명이 되면
            if count >= 5:
                # 출력할 리스트 변수에 넣고
                first_names.append(alphabet)
                # 카운트는 초기화
                count = 0
                # 5명 이상이 있으니 더 이상 이 알파벳에서는 셀 필요가 없다.
                break

    # 한 알파벳에 대한 카운팅이 끝났으니 카운트 변수를 0으로 초기화
    count = 0

# 출력 부분
# 만약 성의 첫 글자가 똑같은 선수가 5명 이상이 하나도 없다면
if len(first_names) == 0:
    # 출력
    print("PREDAJA")
# 성의 첫 글자가 똑같은 선수가 5명 이상인 알파벳이 있다면
else:
    # 순서대로 출력
    for i in first_names:
        print(i, end='')
