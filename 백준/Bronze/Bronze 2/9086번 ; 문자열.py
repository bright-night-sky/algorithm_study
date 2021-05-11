# https://www.acmicpc.net/problem/9086

# 첫 줄에는 테스트 케이스의 개수 T를 입력합니다.
# 1 <= T <= 10
T = int(input())

# 테스트 케이스의 개수만큼 반복합니다.
for i in range(T):
    # 한 문자열을 입력합니다.
    string = input()

    # 문자열의 첫 글자와 마지막 글자를 연속해서 출력합니다.
    print(f"{string[0]}{string[-1]}")