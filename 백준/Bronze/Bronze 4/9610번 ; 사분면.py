# https://www.acmicpc.net/problem/9610

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 첫째 줄에 점의 개수 n을 입력합니다.
# 1 <= n <= 1,000
# 정수형으로 변환합니다.
n = int(stdin.readline())
# 각 사분면과 축에 있는 점의 개수를 저장할 리스트 변수를 선언합니다.
# 인덱스 0에는 축에 있는 점의 개수를
# 인덱스 1 ~ 4에는 각 사분면에 있는 점의 개수를 저장합니다.
q_axis = [0, 0, 0, 0, 0]

# 점의 개수 n만큼 반복합니다.
for point_idx in range(n):
    # 이번 점의 좌표 xi, yi를 공백으로 구분해 입력합니다.
    # -10^6 <= xi, yi <= 10^6
    # 각각 정수형으로 변환합니다.
    xi, yi = map(int, stdin.readline().split(' '))

    # xi가 0보다 크고, yi도 0보다 큰 경우
    if xi > 0 and yi > 0:
        # 1사분면의 점의 개수인 q_axis[1]에 1을 더해줍니다.
        q_axis[1] += 1
    # xi가 0보다 작고, yi는 0보다 큰 경우
    elif xi < 0 and yi > 0:
        # 2사분면의 점의 개수인 q_axis[2]에 1을 더해줍니다.
        q_axis[2] += 1
    # xi가 0보다 작고, yi도 0보다 작은 경우
    elif xi < 0 and yi < 0:
        # 3사분면의 점의 개수인 q_axis[3]에 1을 더해줍니다.
        q_axis[3] += 1
    # xi가 0보다 크고, yi는 0보다 작은 경우
    elif xi > 0 and yi < 0:
        # 4사분면의 점의 개수인 q_axis[4]에 1을 더해줍니다.
        q_axis[4] += 1
    # xi, yi 둘 중 하나가 0이라면
    elif xi == 0 or yi == 0:
        # 축의 점의 개수인 q_axis[0]에 1을 더해줍니다.
        q_axis[0] += 1

# 출력 형식에 맞게 각 사분면과 축의 점의 개수를 출력합니다.
print(f'Q1: {q_axis[1]}')
print(f'Q2: {q_axis[2]}')
print(f'Q3: {q_axis[3]}')
print(f'Q4: {q_axis[4]}')
print(f'AXIS: {q_axis[0]}')