# https://www.acmicpc.net/problem/5524

# 첫째 줄에는 입실 기록의 개수인 정수 N을 입력합니다.
# 1 <= N <= 100
N = int(input())

# 입실 기록의 개수만큼 반복합니다.
for i in range(N):
    # 입실 기록 하나를 입력합니다.
    # 1글자 이상 20글자 이하의 영어 대소문자로만 이루어진 문자열입니다.
    Si = input()

    # 입력한 입실 기록을 모두 소문자로 바꾸고 출력합니다.
    print(Si.lower())