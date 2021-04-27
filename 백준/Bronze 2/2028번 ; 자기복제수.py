# https://www.acmicpc.net/problem/2028

# 첫 줄에는 테스트 케이스의 개수 T를 입력합니다.
# 1 <= T <= 20
T = int(input())

# 테스트 케이스의 개수 T만큼 반복합니다.
for test_case in range(T):
    # 자연수 N을 입력합니다.
    # 1 <= N <= 1000
    N = int(input())

    # N의 제곱을 구하고 문자열 형태로 저장한 변수를 선언합니다.
    N_square = str(N * N)

    # 자연수 N의 길이를 저장하는 변수를 선언합니다.
    N_length = len(str(N))

    # N의 제곱에서 맨 뒷자리의 숫자가 N과 같다면
    if N_square[-N_length:] == str(N):
        # YES를 출력합니다.
        print("YES")
    # N의 제곱에서 맨 뒷자리의 숫자가 N과 다르다면
    else:
        # NO를 출력합니다.
        print("NO")