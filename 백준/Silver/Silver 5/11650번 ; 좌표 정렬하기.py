# https://www.acmicpc.net/problem/11650

# 첫째 줄에 점의 개수 N을 입력합니다.
# 1 <= N <= 100,000
N = int(input())

# 점들의 좌표를 저장하는 리스트 변수를 선언합니다.
points = []

# 점의 개수 N만큼 반복합니다.
for point_index in range(N):
    # 점의 위치 xi와 yi를 공백으로 구분해 입력합니다.
    # -100,000 <= xi, yi <= 100,000
    # xi, yi는 정수형으로 변환해줍니다.
    point = list(map(int, input().split(' ')))

    # 입력한 점의 좌표를 points 리스트 변수에 넣어줍니다.
    points.append(point)

# 점들을 x좌표와 y좌표를 기준으로 오름차순 정렬을 해줍니다.
points.sort(key=lambda point: (point[0], point[1]))

# 정렬이 된 점들을 x좌표 y좌표 형식으로 하나씩 출력해줍니다.
for point in points:
    print(point[0], point[1])