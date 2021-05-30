# https://www.acmicpc.net/problem/11651

# readline을 사용하기 위해 import합니다.
from sys import stdin

# 첫째 줄에 점의 개수 N을 입력합니다.
# 1 <= N <= 100,000
# 정수형으로 변환합니다.
N = int(stdin.readline())
# 각 점의 x좌표, y좌표 리스트를 저장할 리스트 변수를 선언합니다.
# N개의 None으로 초기화합니다.
points = [None] * N

# 점의 개수 N만큼 반복합니다.
for point_idx in range(N):
    # i번 점의 위치 xi, yi를 공백으로 구분해 입력합니다.
    # -100,000 <= xi, yi <= 100,000
    # 각각 정수형으로 변환하고 함께 리스트 변수로 만들어 준 후
    # points에 넣어줍니다.
    points[point_idx] = list(map(int, stdin.readline().split(' ')))

# points에 있는 점을 y좌표가 증가하는 순으로 y좌표가 같으면 x좌표가 증가하는 순서로 정렬합니다.
points.sort(key=lambda point: (point[1], point[0]))

# 정렬된 점들을 출력 형식에 맞게 하나씩 출력합니다.
for point in points:
    print(point[0], point[1])