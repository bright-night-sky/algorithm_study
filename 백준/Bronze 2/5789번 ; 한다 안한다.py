# https://www.acmicpc.net/problem/5789

# 첫째 줄에는 테스트 케이스의 개수 N을 입력합니다.
# 1 <= N <= 1000
N = int(input())

# 테스트 케이스의 개수만큼 반복해봅니다.
for i in range(N):
    # 0과 1로 이루어진 문자열을 입력합니다.
    # 문자열의 길이는 항상 짝수이고, 1000보다 작습니다.
    string = input()

    # 입력한 문자열의 길이의 절반을 저장하는 변수를 선언합니다.
    half_len = int(len(string) / 2)

    # 상근이가 마지막으로 고르는 두 숫자는 입력한 문자열에서 가운데 두 숫자입니다.
    # 가운데 두 숫자가 같은 경우
    if string[half_len - 1] == string[half_len]:
        # Do-it을 출력합니다.
        print("Do-it")
    # 가운데 두 숫자가 다른 경우
    else:
        # Do-it-Not을 출력합니다.
        print("Do-it-Not")