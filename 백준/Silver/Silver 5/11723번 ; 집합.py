# https://www.acmicpc.net/problem/11723

# readline을 사용하기 위해 import합니다.
from sys import stdin

# 공집합 S를 만들어줍니다.
S = set()
# 첫째 줄에 수행해야 하는 연산의 수 M을 입력합니다.
# 1 <= M <= 3,000,000
# 정수형으로 변환합니다.
M = int(stdin.readline())

# 연산의 수 M만큼 반복합니다.
for calculation_idx in range(M):
    # 연산 한 줄을 입력합니다.
    # 공백으로 구분해줍니다.
    calculation = stdin.readline().rstrip().split(' ')

    # 연산이 add라면
    if calculation[0] == 'add':
        # x인 calculation[1]를 정수형으로 변환해서 집합 S에 추가합니다.
        S.add(int(calculation[1]))
    # 연산이 remove라면
    elif calculation[0] == 'remove':
        # x인 calculation[1]를 정수형으로 변환해서 집합 S에서 제거 시도해봅니다.
        try:
            # 집합 S에 x인 calculation[1]이 있다면 제거합니다.
            S.remove(int(calculation[1]))
        # calculation[1]이 집합 S에 없어서 KeyError가 뜬다면
        except KeyError:
            # 연산을 무시합니다.
            pass
    # 연산이 check라면
    elif calculation[0] == 'check':
        # 집합 S에 x인 정수형 calculation[1]이 있다면
        if int(calculation[1]) in S:
            # 1을 출력합니다.
            print(1)
        # 집합 S에 x인 정수형 calculation[1]이 없다면
        else:
            # 0을 출력합니다.
            print(0)
    # 연산이 toggle이라면
    elif calculation[0] == 'toggle':
        # # 집합 S에 x인 정수형 calculation[1]이 있다면
        if int(calculation[1]) in S:
            # 집합 S에서 x인 정수형 calculation[1]을 제거합니다.
            S.remove(int(calculation[1]))
        # # 집합 S에 x인 정수형 calculation[1]이 없다면
        else:
            # 집합 S에서 x인 정수형 calculation[1]을 추가합니다.
            S.add(int(calculation[1]))
    # 연산이 all이라면
    elif calculation[0] == 'all':
        # 집합 S를 정수 1부터 20까지 숫자로 채워줍니다.
        S = {number for number in range(1, 21)}
    # 연산이 empty라면
    elif calculation[0] == 'empty':
        # 집합 S를 공집합으로 만듭니다.
        S = set()