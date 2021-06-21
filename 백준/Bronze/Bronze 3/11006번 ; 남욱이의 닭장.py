# https://www.acmicpc.net/problem/11006

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 첫째 줄에 총 테스트 케이스의 수 T를 입력합니다.
# T <= 25
# 정수형으로 변환합니다.
T = int(stdin.readline())

# 테스트 케이스의 수 T만큼 반복합니다.
for test_case_idx in range(T):
    # 모든 닭의 다리수의 합 N, 닭의 수 M을 공백으로 구분해 입력합니다.
    # 1 <= N <= 300
    # M <= N <= 2M
    N, M = map(int, stdin.readline().split(' '))
    # 모든 닭의 다리가 멀쩡할 때의 다리수를 저장하는 변수를 선언합니다.
    origin_legs = M * 2
    # 다리가 잘린 닭의 수 U를 선언합니다.
    # 다리를 잃은 닭은 모두 한쪽 다리만 잃으므로,
    # 다리가 잘린 닭의 수는 원래 다리수에서 지금의 모든 닭의 다리수의 합을 뺀 값입니다.
    U = origin_legs - N
    # 멀쩡한 닭의 수 T를 선언합니다.
    # 모든 닭의 수에서 다리가 잘린 닭의 수 U를 뺍니다.
    T = M - U

    # 출력 형식에 맞게 다리가 잘린 닭의 수와 멀쩡한 닭의 수를 공백으로 구분해 출력합니다.
    print(U, T)
