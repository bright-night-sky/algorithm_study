# https://www.acmicpc.net/problem/5988

# 첫 번째 줄에 숫자의 개수 N을 입력합니다.
# 1 <= N <= 100
N = int(input())

# 숫자의 개수만큼 반복합니다.
for i in range(N):
    # 홀수인지 짝수인지 확인할 정수 K를 입력합니다.
    # 1 <= K <= 10^60
    K = int(input())

    # K를 2로 나누었을 때 나머지가 0이라면
    if K % 2 == 0:
        # 짝수이므로 even을 출력합니다.
        print("even")
    # K를 2로 나누었을 때 나머지가 1이라면
    else:
        # 홀수이므로 odd를 출력합니다.
        print("odd")