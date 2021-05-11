# https://www.acmicpc.net/problem/11365

# END를 입력할 때까지 계속 반복합니다.
while True:
    # 암호문을 하나 입력합니다.
    # 암호의 길이는 500을 넘지 않습니다.
    cryptogram = input()

    # 입력한 암호문이 END라면
    if cryptogram == "END":
        # 해독하지 않고 그냥 반복문을 탈출하고 끝냅니다.
        break
    # 다른 암호문을 입력했다면
    else:
        # 암호문을 거꾸로 출력합니다.
        print(cryptogram[::-1])