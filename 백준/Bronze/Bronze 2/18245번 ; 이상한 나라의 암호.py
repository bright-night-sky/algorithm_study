# https://www.acmicpc.net/problem/18245

# i번째 줄에서 i를 저장하는 변수를 선언합니다.
count = 1

# Was it a cat I saw?를 입력할 때까지 반복합니다.
while True:
    # 한 문장을 입력합니다.
    sentence = input()

    # 만약 입력한 문장이 Was it a cat I saw?라면
    if sentence == "Was it a cat I saw?":
        # 반복문을 탈출합니다.
        break

    # 현재 문장을 i칸씩 건너뛰며 출력합니다.
    print(sentence[::count+1])

    # i번째에 1을 더해줍니다.
    count += 1