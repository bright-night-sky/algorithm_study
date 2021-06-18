# https://www.acmicpc.net/problem/7510

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 첫째 줄에 테스트 케이스의 개수 n을 입력합니다.
# 정수형으로 변환합니다.
n = int(stdin.readline())

# 테스트 케이스의 개수 n만큼 반복합니다.
for i in range(n):
    # 세 정수 a, b, c를 공백으로 구분해 입력합니다.
    # 1 <= a, b, c <= 40,000
    # 각각 정수형으로 변환하고 리스트 변수에 넣어줍니다.
    numbers = list(map(int, stdin.readline().split(' ')))
    # numbers를 오름차순으로 정렬합니다.
    numbers.sort()
    # 직각 삼각형인지 아닌지의 여부를 저장할 변수를 선언합니다.
    is_right_angled = None

    # 직각 삼각형 조건을 만족한다면
    if numbers[0] ** 2 + numbers[1] ** 2 == numbers[2] ** 2:
        # is_right_angled에 yes를 저장합니다.
        is_right_angled = 'yes'
    # 직각 삼각형 조건을 만족하지 않는다면
    else:
        # is_right_angled에 no를 저장합니다.
        is_right_angled = 'no'

    # 출력 형식에 맞게 출력합니다.
    print(f'Scenario #{i+1}:')
    print(is_right_angled)
    print()