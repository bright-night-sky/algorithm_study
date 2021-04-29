# https://www.acmicpc.net/problem/11170

# 첫 번째 줄에 테스트 케이스의 수 T를 입력합니다.
# 1 <= T <= 20
T = int(input())

# 테스트 케이스의 수 T만큼 반복합니다.
for test_case in range(T):
    # N, M을 입력합니다.
    # 0 <= N <= M <= 1,000,000
    # 정수형으로 변환해서 변수에 저장합니다.
    N, M = map(int, input().split(' '))

    # 0의 개수를 저장하는 변수를 선언합니다.
    zero_count = 0

    # N부터 M까지 반복해봅니다.
    for num in range(N, M + 1):
        # 현재 숫자를 문자열 형태로 저장하는 변수를 선언합니다.
        str_num = str(num)

        # 현재 숫자에서 0의 개수를 세어 zero_count에 더해줍니다.
        zero_count += str_num.count('0')

    # 최종적으로 0의 개수를 출력합니다.
    print(zero_count)