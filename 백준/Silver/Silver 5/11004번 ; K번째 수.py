# https://www.acmicpc.net/problem/11004

# readline을 사용하기 위해 import합니다.
from sys import stdin

# 첫째 줄에 N, K를 공백으로 구분해 입력합니다.
# 1 <= N <= 5,000,000
# 1 <= K <= N
# 각각 정수형으로 변환합니다.
N, K = map(int, stdin.readline().split(' '))
# 둘째 줄에는 A1, A2, ..., AN을 공백으로 구분해 입력합니다.
# -10^9 <= Ai <= 10^9
# 각각 정수형으로 변환하고 리스트 변수에 넣은 뒤, 오름차순으로 정렬합니다.
sorted_numbers = sorted(list(map(int, stdin.readline().split(' '))))

# 앞에서부터 K번째 있는 수를 출력합니다.
print(sorted_numbers[K - 1])