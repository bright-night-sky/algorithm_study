# https://www.acmicpc.net/problem/20053

# 첫째 줄에 테스트 케이스의 개수 T를 입력합니다.
# 1 <= T <= 10
T = int(input())

# 각 테스트 케이스를 실행합니다.
for i in range(0, T):
    # 각 테스트 케이스는 두 줄로 이루어져 있습니다.
    # 첫째 줄에 정수의 개수 N을 입력합니다.
    # 1 <= N <= 1,000,000
    N = int(input())

    # 둘째 줄에는 N개의 정수를 공백으로 구분해서 입력합니다.
    # 모든 정수는 -1,000,000보다 크거나 같고, 1,000,000보다 작거나 같습니다.
    nums = list(map(int, input().split(' ')))

    # 최댓값과 최솟값을 저장하는 변수입니다.
    max_num = max(nums)
    min_num = min(nums)

    # 이번 케이스의 최댓값과 최솟값을 출력합니다.
    print(min_num, max_num)