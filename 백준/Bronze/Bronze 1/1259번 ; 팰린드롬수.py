# https://www.acmicpc.net/problem/1259

# 테스트 케이스에 0을 입력할 때까지 계속 입력받는다.
while True:
    # 한 테스트 케이스 입력
    num = input()

    # 입력한 테스트 케이스가 0인 경우
    if num == '0':
        # 팰린드롬수 테스트 종료
        break

    # 입력받은 테스트 케이스가 팰린드롬이라면
    if num == num[::-1]:
        # yes 출력
        print("yes")
    # 입력받은 테스트 케이스가 팰린드롬이 아니라면
    else:
        # no 출력
        print("no")