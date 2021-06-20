# https://www.acmicpc.net/problem/10833

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 첫째 줄에는 학교의 수를 나타내는 정수 N을 입력합니다.
# 1 <= N <= 100
# 정수형으로 변환합니다.
N = int(stdin.readline())
# 남은 사과의 총 개수를 저장할 변수를 선언합니다.
# 0으로 초기화합니다.
remain_apples = 0

# 학교의 수 N만큼 반복합니다.
for school_idx in range(N):
    # 학교의 학생 수와 사과 개수를 공백으로 구분해 입력합니다.
    # 학생 수와 사과 개수 모두 1 이상 100 이하입니다.
    # 각각 정수형으로 변환합니다.
    students, apples = map(int, stdin.readline().split(' '))

    # 사과 개수를 학생 수로 나눈 뒤 나온 나머지를 남은 사과의 총 개수에 더해줍니다.
    remain_apples += apples % students

# 남은 사과의 총 개수를 출력합니다.
print(remain_apples)