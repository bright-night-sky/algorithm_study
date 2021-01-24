# https://www.acmicpc.net/problem/3154

# 각 번호의 좌표를 저장하는 dictionary입니다.
num_coor = {
    1: [0, 0],
    2: [1, 0],
    3: [2, 0],
    4: [0, 1],
    5: [1, 1],
    6: [2, 1],
    7: [0, 2],
    8: [1, 2],
    9: [2, 2],
    0: [1, 3]
}

# 문제에서 나오는 effort 함수를 정의합니다.
def effort(a, b):
    return abs(num_coor[a][0] - num_coor[b][0]) + abs(num_coor[a][1] - num_coor[b][1])

# 입력 첫 번째 줄에는 HH:MM 형식으로 설정하고 싶은 시각을 입력합니다.
# 만약 시간이나 분이 한 자리수라면 선행하는 0이 붙어야 합니다.
# 시와 분을 각각의 변수에 저장합니다.
hour, min = map(int, input().split(':'))

# 가장 적은 노력의 값을 저장하는 변수입니다.
# -1로 초기화해줍니다.
min_effort = -1




# 시와 분의 십의 자리와 일의 자리를 각각 변수로 저장합니다.
hour_ten = hour[0]
hour_one = hour[1]
min_ten = min[0]
min_one = min[1]

