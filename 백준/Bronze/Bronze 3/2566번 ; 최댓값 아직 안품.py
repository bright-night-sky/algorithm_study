# https://www.acmicpc.net/problem/2566

# 2차원 배열 선언
grid = []
# 최댓값의 행과 열을 저장할 변수
column = 0
row = 0
# 각 행의 배열의 최댓값들을 저장할 임시 변수
column_max = []
# 각 행의 배열의 최댓값들 중 가장 큰 최댓값을 가진 행 배열이 몇 번째인지 저장할 변수
column_max_idx = -1
#

# 9X9에 자연수를 입력
for i in range(0, 9):
    grid.append(list(map(int, input().split(' '))))

# 각 행의 배열의 최댓값을 추출하고 column_max 배열에 저장
for i in grid:
    column_max.append(max(i))



# 격자판에서 제일 큰 값 출력
print(max(column_max))