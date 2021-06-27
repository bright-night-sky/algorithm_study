# https://www.acmicpc.net/problem/11908

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 첫 번째 줄에 카드의 수를 나타내는 자연수 n을 입력합니다.
# 1 <= n <= 2,222
# 정수형으로 변환합니다.
n = int(stdin.readline())
# 두 번째 줄에 카드에 적힌 숫자들 c1, c2, ..., cn을 공백을 사이에 두고 입력합니다.
# 각각 정수형으로 변환하고 리스트 변수에 넣어줍니다.
c = list(map(int, stdin.readline().split(' ')))
# 카드에 있는 숫자들을 모두 더한 값을 저장하는 변수를 선언합니다.
c_sum = sum(c)
# 카드에 있는 숫자들 중 가장 큰 숫자를 저장하는 변수를 선언합니다.
c_max = max(c)

# 문제의 행동을 반복한 뒤, 가능한 최대 합은 c_sum에서 c_max를 뺀 값이므로 그 값을 출력합니다.
print(c_sum - c_max)