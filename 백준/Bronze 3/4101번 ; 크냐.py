# https://www.acmicpc.net/problem/4101

# 0 0을 입력할 때까지 실행
while True:
    # 두 정수 입력
    # 백만보다 작거나 같은 양의 정수
    num1, num2 = map(int, input().split(' '))

    # 0 0을 입력했다면
    if num1 == num2 == 0:
        # 반복문 탈출
        break

    # 첫 번째 수가 두 번째 수보다 크다면
    if num1 > num2:
        # Yes 출력
        print("Yes")
    # 첫 번째 수가 두 번째 수보다 크지 않다면
    else:
        # No 출력
        print("No")