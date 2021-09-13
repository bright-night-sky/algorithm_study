# https://codeup.kr/problem.php?id=1277

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 첫 줄에 데이터의 개수 N을 입력합니다.
# N은 N >= 1인 홀수입니다.
# int형으로 변환합니다.
N = int(stdin.readline())
# 그 다음 줄에 N개의 데이터를 공백으로 구분해 입력합니다.
# 각각 int형으로 변환하고, 리스트 변수에 넣어줍니다.
data = list(map(int, stdin.readline().split()))

# 첫 번째 데이터, 중간 데이터, 마지막 데이터를 공백으로 구분해 출력합니다.
print(data[0], data[N // 2], data[-1])