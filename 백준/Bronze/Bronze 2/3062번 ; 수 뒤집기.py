# https://www.acmicpc.net/problem/3062

# 첫 줄에는 테스트 케이스의 개수 T를 입력합니다.
T = int(input())

# 테스트 케이스의 개수만큼 반복합니다.
for i in range(T):
    # 정수 N을 입력합니다.
    # 지금은 문자열 형태가 필요하므로 바로 정수형으로 변환하지는 않습니다.
    # 10 <= N <= 100000
    N = input()

    # 입력받은 N을 뒤집은 숫자를 reversed_N 변수에 저장합니다.
    reversed_N = int(N[::-1])
    # 위의 N도 정수형으로 만들어줍니다.
    N = int(N)

    # N과 reversed_N을 더하고 문자열로 만들어 sum 변수에 저장합니다.
    sum = str(N + reversed_N)

    # 원래수 sum과 뒤집은 수가 같다면
    if sum == sum[::-1]:
        # YES를 출력합니다.
        print("YES")
    # 그렇지 않다면
    else:
        # NO를 출력합니다.
        print("NO")