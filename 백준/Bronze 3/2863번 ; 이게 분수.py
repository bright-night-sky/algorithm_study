# https://www.acmicpc.net/problem/2863

# 첫째 줄에 A와 B를 공백으로 구분해서 입력합니다.
A, B = map(int, input().split(' '))
# 둘째 줄에 C와 D를 공백으로 구분해서 입력합니다.
C, D = map(int, input().split(' '))

# 표의 값의 최댓값을 저장하는 변수입니다.
table_max = 0

# 표의 값이 최댓값이 되었을 때의 회전수를 저장하는 변수입니다.
turn_count = 0

# 표의 모양이 다른 경우는 4가지뿐입니다.
# 표의 모양이 다를 때의 값을 계산하여 최댓값을 출력하면 됩니다.

# 표의 모양이 다른 4가지 경우에서 표의 값을 계산하여 최댓값인지 비교해봅니다.
for i in range(0, 4):
    # 표의 값을 계산합니다.
    table_value = A / C + B / D

    # 현재 표의 모양에서 계산한 값이 이전까지의 표의 값의 최댓값보다 크다면
    if table_value > table_max:
        # 최댓값을 현재 표의 값으로 저장합니다.
        table_max = table_value
        # 현재 표의 모양에서의 회전수를 저장합니다.
        turn_count = i

    # 다음 표의 모양으로 만들어줍니다.
    temp = A
    A = C
    C = D
    D = B
    B = temp

# 표의 값이 최댓값일 때의 회전수를 출력합니다.
print(turn_count)