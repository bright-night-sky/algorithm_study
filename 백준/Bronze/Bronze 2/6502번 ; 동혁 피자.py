# https://www.acmicpc.net/problem/6502

# 피자의 순서를 저장하는 변수를 선언합니다.
pizza_index = 1

# 0을 입력할 때까지 반복합니다.
while True:
    # 이번 테스트 케이스를 입력합니다.
    test_case = input()

    # 0을 입력했다면
    if test_case == '0':
        # 반복문을 탈출하고 종료합니다.
        break
    # 숫자 세 개를 입력했다면
    else:
        # r, w, l을 공백으로 구분해 입력합니다.
        # r, w, l은 정수형으로 변환합니다.
        # 1 <= r <= 1000
        # 1 <= w <= l <= 1000
        r, w, l = map(int, test_case.split(' '))

        # 식탁의 지름을 저장하는 변수를 선언합니다.
        diameter = 2 * r

        # 피자의 대각선 길이를 저장하는 변수를 선언합니다.
        diagonal = (w ** 2 + l ** 2) ** 0.5

        # 식탁의 지름이 피자의 대각선보다 크거나 같다면
        if diameter >= diagonal:
            # 이번 피자는 식탁에 맞는 크기이므로 출력 형식에 맞게 출력합니다.
            print(f"Pizza {pizza_index} fits on the table.")
        # 식탁의 지름이 피자의 대각선보다 작다면
        else:
            # 이번 피자는 식탁에 맞지 않는 크기이므로 출력 형식에 맞게 출력합니다.
            print(f"Pizza {pizza_index} does not fit on the table.")

        # 피자의 순서에 1을 더해줍니다.
        pizza_index += 1