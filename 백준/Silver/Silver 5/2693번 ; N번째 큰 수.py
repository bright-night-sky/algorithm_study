# https://www.acmicpc.net/problem/2693

# 첫째 줄에 테스트 케이스의 개수 T를 입력합니다.
# 1 <= T <= 1,000
T = int(input())

# 테스트 케이스의 개수 T만큼 반복합니다.
for test_case_index in range(T):
    # 배열 A의 원소 10개를 공백으로 구분해 입력합니다.
    # 각 원소를 정수형으로 변환해서 리스트 변수에 넣어줍니다.
    A = list(map(int, input().split(' ')))

    # 3번째로 큰 수를 찾기 위해 내림차순으로 정렬합니다.
    A.sort(reverse=True)

    # 배열 A에서 3번째로 큰 수를 출력합니다.
    print(A[2])