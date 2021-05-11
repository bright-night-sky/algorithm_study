# https://www.acmicpc.net/problem/4504

# 정수 n 입력
# 0 < n < 1000
n = int(input())

# 0이 입력될 때까지 반복
while True:
    # 숫자 하나씩 입력
    num = int(input())

    # 만약 0이 입력되었다면
    if num == 0:
        # 반복문 탈출
        break

    # 만약 입력한 num이 n의 배수이면
    if num % n == 0:
        # 배수가 맞다고 출력
        print(f"{num} is a multiple of {n}.")
    # 만약 입력한 num이 n의 배수가 아니면
    else:
        # 배수가 아니라고 출력력
        print(f"{num} is NOT a multiple of {n}.")
