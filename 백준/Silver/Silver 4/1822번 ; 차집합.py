# https://www.acmicpc.net/problem/1822

# readline을 사용하기 위해 import합니다.
from sys import stdin

# 첫째 줄에 집합 A의 원소의 개수 n(A), 집합 B의 원소의 개수 n(B)를 빈 칸을 사이에 두고 입력합니다.
# 1 <= n(A), n(B) <= 500,000
# 각각 정수형으로 변환합니다.
nA, nB = map(int, stdin.readline().split(' '))
# 둘째 줄에는 집합 A의 원소를 빈 칸을 사이에 두고 입력합니다.
# 각각 정수형으로 변환하고 set 변수에 넣어줍니다.
A = set(map(int, stdin.readline().split(' ')))
# 셋째 줄에는 집합 B의 원소를 빈 칸을 사이에 두고 입력합니다.
# 각각 정수형으로 변환하고 set 변수에 넣어줍니다.
# 집합의 원소는 2,147,473,647 이하의 자연수입니다.
# 한 집합의 모든 원소의 값은 다릅니다.
B = set(map(int, stdin.readline().split(' ')))
# 집합 A에는 속하면서 집합 B에는 속하지 않는 set를 만듭니다.
# 리스트 변수로 만들고 오름차순 정렬을 해줍니다.
A_diff_B = sorted(list(A.difference(B)))

# A_diff_B 원소의 개수를 출력합니다.
print(len(A_diff_B))
# A_diff_B 원소의 개수가 0이 아니라면
if len(A_diff_B) != 0:
    # 출력 형식에 맞게 원소를 하나씩 출력합니다.
    for element in A_diff_B:
        print(element, end=' ')