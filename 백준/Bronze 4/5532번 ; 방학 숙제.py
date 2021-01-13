# https://www.acmicpc.net/problem/5532

import math

# 방학 총 일수 : L
# 국어 총 A 페이지
# 수학 총 B 페이지
# 상근이는 하루에 국어를 최대 C페이지, 수학을 최대 D 페이지 풀 수 있다.
# 다섯 줄에 걸쳐 L, A, B, C, D 입력
# 2 <= L <= 40
# 1 <= A, B <= 1000
# 1 <= C, D <= 100

L = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())
# 항상 방학 숙제를 방학 기간 내에 다 할 수 있는 경우만 입력으로 주어진다.
# 즉, 방학 숙제를 다 못하는 경우는 없다.

# 국어를 다 푸는 데 걸리는 일수를 저장하는 변수
complete_korean = math.ceil(A / C)
# 수학을 다 푸는 데 걸리는 일수를 저장하는 변수
complete_math = math.ceil(B / D)
# 국어와 수학 중 다 푸는데 걸리는 일수가 더 긴 과목의 일수를 저장하는 변수
more_day = 0
# 수학보다 국어를 다 푸는데 걸리는 일수가 더 길면
if complete_korean > complete_math:
    # 국어를 다 푸는데 걸리는 일수를 저장
    more_day = complete_korean
# 국어보다 수학을 다 푸는데 걸리는 일수가 더 길면
else:
    # 수학을 다 푸는데 걸리는 일수를 저장
    more_day = complete_math

# 놀 수 있는 최대의 날수는 (방학 일수) - (푸는데 걸리는 일수가 더 긴 과목의 일수)이다.
print(L - more_day)