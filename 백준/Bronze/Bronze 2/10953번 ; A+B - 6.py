# https://www.acmicpc.net/problem/10953

# 첫째 줄에 테스트 케이스의 개수 T를 입력합니다.
T = int(input())

# 테스트 케이스의 개수 T만큼 반복합니다.
for test_case_index in range(T):
    # 테스트 케이스 한 줄을 입력합니다.
    # 입력받은 테스트 케이스를 ,로 구분하고 정수형으로 바꾼 뒤 A, B에 넣어줍니다.
    A, B = map(int, input().split(','))

    # A, B의 합을 출력합니다.
    print(A + B)