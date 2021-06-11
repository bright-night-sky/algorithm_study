# https://www.acmicpc.net/problem/14648

# readline을 사용하기 위해 import합니다.
from sys import stdin

# 첫째 줄에 수열의 길이 n, 쿼리의 개수 q를 공백으로 구분해 입력합니다.
# 1 <= n <= 1,000
# 1 <= q <= 10,000
# 각각 정수형으로 변환합니다.
n, q = map(int, stdin.readline().split(' '))
# 둘째 줄에 길이 n의 수열의 값들을 공백으로 구분해 입력합니다.
# 각각 정수형으로 변환합니다.
numbers = list(map(int, stdin.readline().split(' ')))

# 쿼리의 개수 q만큼 반복합니다.
for query_idx in range(q):
    # 쿼리를 입력합니다.
    # 각 값들을 공백으로 구분해줍니다.
    query = list(map(int, stdin.readline().split(' ')))
    # query의 첫 번째 값인 쿼리의 종류를 저장하는 변수를 선언합니다.
    type = query[0]

    # 쿼리의 종류가 1이라면
    if type == 1:
        # 문제의 a, b를 뜻하는 값들을 선언합니다.
        a, b = query[1], query[2]
        # 수열의 [a, b] 구간의 합을 출력합니다.
        print(sum(numbers[a-1:b]))
        # 수열에서 a번째 숫자와 b번째 숫자를 서로 바꿔줍니다.
        numbers[a-1], numbers[b-1] = numbers[b-1], numbers[a-1]
    # 쿼리의 종류가 2라면
    else:
        # 문제의 a, b, c, d를 뜻하는 값들을 선언합니다.
        a, b, c, d = query[1], query[2], query[3], query[4]
        # [a, b] 구간의 합을 저장하는 변수를 선언합니다.
        ab_sum = sum(numbers[a-1:b])
        # [c, d] 구간의 하을 저장하는 변수를 선언합니다.
        cd_sum = sum(numbers[c-1:d])
        # ab_sum에서 cd_sum를 뺀 값을 출력합니다.
        print(ab_sum - cd_sum)