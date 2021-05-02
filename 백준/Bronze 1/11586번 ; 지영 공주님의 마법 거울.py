# https://www.acmicpc.net/problem/11586

# 첫 번째 줄에 정사각형 모양의 마법거울의 크기를 나타내는 자연수 N을 입력합니다.
# 2 <= N <= 100
N = int(input())

# 지영 공주님의 원래 모습을 저장하는 리스트 변수를 선언합니다.
magic_mirror = []

# 마법거울의 크기 N만큼 반복합니다.
for row_index in range(N):
    # 지영 공주님의 원래 모습 한 줄을 입력합니다.
    # 알파벳 대소문자로만으로 표현합니다.
    row = input()

    # 지영 공주님의 원래 모습 한 줄을 magic_mirror 리스트 변수에 넣어줍니다.
    magic_mirror.append(row)

# 마법거울의 심리상태 K를 입력합니다.
# 1 <= K <= 3
K = input()

# 마법거울의 심리상태가 1이라면
if K == '1':
    # 거울에 비친 지영 공주님의 원래 모습을 그대로 출력합니다.
    for row in magic_mirror:
        print(row)
# 마법거울의 심리상태가 2라면
elif K == '2':
    # 거울에 비친 지영 공주님의 원래 모습을 좌/우로 반전된 모습으로 출력합니다.
    for row in magic_mirror:
        # 한 줄마다 거꾸로 출력하면 됩니다.
        print(row[::-1])
# 마법거울의 심리상태가 3이라면
else:
    # 거울에 비친 지영 공주님의 원래 모습을 상/하로 반전된 모습으로 출력합니다.
    for row_index in range(-1, -N-1, -1):
        # magic_mirror에 저장된 한 줄씩의 데이터를 반대로 출력하면 됩니다.
        print(magic_mirror[row_index])