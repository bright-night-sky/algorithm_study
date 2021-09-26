# https://codeup.kr/problem.php?id=1293

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 첫 번째 줄에 점수의 개수 n을 입력합니다.
# 2 <= n <= 100
n = stdin.readline()
# n개의 점수를 공백으로 구분해 입력합니다.
# 각 점수의 범위는 0 ~ 100입니다.
# 각각 int형으로 변환하고 리스트 변수에 넣어줍니다.
scores = list(map(int, stdin.readline().split()))
# scores에서 최댓값을 구하고 변수에 저장합니다.
max_score = max(scores)
# scores에서 최솟값을 구하고 변수에 저장합니다.
min_score = min(scores)

# n개의 점수 중 최댓값과 최솟값을 공백으로 구분해 출력합니다.
print(max_score, min_score)