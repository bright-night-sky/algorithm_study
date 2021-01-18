# https://www.acmicpc.net/problem/14264

import math

# 정육각형 한 변의 길이 L 입력
# 1 <= L <= 1,000,000인 정수
L = int(input())

# 제일 작은 삼각형의 밑변 길이
bottom = L * math.sqrt(3)

# 제일 작은 삼각형의 높이 길이
height = L * 0.5

# 제일 작은 삼각형의 넓이
area = 0.5 * bottom * height

# 결과 출력
# 절대/상대 오차는 10^-9까지 허용한다.
print(area)