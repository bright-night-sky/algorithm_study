# https://www.acmicpc.net/problem/17838

# 첫 줄에는 테스트 케이스의 개수 T를 입력합니다.
# 1 <= T <= 100
T = int(input())

# 테스트 케이스의 개수만큼 반복합니다.
for i in range(T):
    # 길이가 N이고, 알파벳 대문자로만 이루어진 문자열을 입력합니다.
    # N은 10,000보다 작거나 같은 자연수입니다.
    string = input()

    # 커맨드의 조건인 1. 문자열의 길이는 7이고,
    # 문자열은 정확히 2가지 종류의 문자로 이루어져 있으며
    # AABBABB 형식을 만족한다면
    if len(string) == 7 and (string[0] == string[1] == string[4]) and (string[2] == string[3] == string[5] == string[6]) and (string[0] != string[2]):
        # 1을 출력합니다.
        print(1)
    # 위의 조건을 만족하지 않는다면
    else:
        # 0을 출력합니다.
        print(0)