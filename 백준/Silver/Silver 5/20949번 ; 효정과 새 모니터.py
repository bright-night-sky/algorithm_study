# https://www.acmicpc.net/problem/20949

# sqrt 함수를 사용하기 위해 import 해줍니다.
from math import sqrt

# 첫 번째 줄에 모니터의 개수 N을 입력합니다.
# 1 <= N <= 1,000
# 정수입니다.
N = int(input())

# 각 모니터의 번호와 PPI를 저장할 리스트 변수를 선언합니다.
monitors = []

# 모니터의 개수 N만큼 반복해봅니다.
for monitor_index in range(N):
    # i번 모니터의 가로 픽셀 수 Wi, 세로 픽셀 수 Hi를 공백으로 구분해 입력합니다.
    # 1 <= Wi, Hi <= 30,000
    # 정수입니다.
    Wi, Hi = map(int, input().split(' '))
    # PPI를 계산하는 공식의 결과를 저장하는 변수를 선언합니다.
    # 문제에서 77인치 모니터를 구매할 것이라고 했으므로 D는 77입니다.
    PPI = sqrt(Wi ** 2 + Hi ** 2) / 77

    # 이번 모니터의 모니터 번호, PPI를 리스트로 만들고, monitors에 넣어줍니다.
    monitors.append([monitor_index + 1, PPI])

# monitors 내부의 값들을 PPI가 높은 순인 내림차순으로 먼저 정렬하고,
# PPI가 동일한 경우에는 모니터의 번호가 더 작은 순인 오름차순으로 정렬합니다.
monitors.sort(key=lambda monitor: (-monitor[1], monitor[0]))

# 출력 형식에 맞게 각 모니터의 번호를 출력합니다.
for monitor in monitors:
    print(monitor[0])