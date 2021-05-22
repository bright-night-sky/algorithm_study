# https://www.acmicpc.net/problem/6322

# readline을 사용하기 위해 import합니다.
from sys import stdin

# 테스트 케이스의 번호를 저장하는 변수를 선언합니다.
idx = 1
# 반복문을 계속 돌려봅니다.
while True:
    # 직각 삼각형 세 변의 길이 a, b, c를 공백으로 구분해 입력합니다.
    # 하나는 -1입니다.
    # 다른 두 수는 10,000보다 작거나 같은 자연수입니다.
    # 각각 정수형으로 변환해줍니다.
    a, b, c = map(int, stdin.readline().split(' '))

    # 입력한 a, b, c가 모두 0이라면
    if a == b == c == 0:
        # 반복문을 탈출합니다.
        break

    # -1로 주어진 변의 길이를 저장할 변수를 선언합니다.
    result = None
    # -1이 입력된 변의 이름 a, b, c 중 하나를 저장하는 변수를 선언합니다.
    minus_one = None

    # a가 -1이라면
    if a == -1:
        # minus_one에 a를 저장해줍니다.
        minus_one = "a"
        # 빗변 c의 제곱에서 밑변 b의 제곱을 빼준 값을 저장하는 변수를 선언합니다.
        result = (c ** 2 - b ** 2)
    # b가 -1이라면
    elif b == -1:
        # minus_one에 b를 저장해줍니다.
        minus_one = "b"
        # 빗변 c의 제곱에서 높이 a의 제곱을 빼준 값을 저장하는 변수를 선언합니다.
        result = (c ** 2 - a ** 2)
    # c가 -1이라면
    else:
        # minus_one에 c를 저장해줍니다.
        minus_one = "c"
        # 높이 a의 제곱과 밑변 b의 제곱을 더한 값을 저장하는 변수를 선언합니다.
        result = (a ** 2 + b ** 2)

    # 출력 형식에 맞게 출력합니다.
    print(f"Triangle #{idx}")
    # result가 0보다 작거나 같다면
    if result <= 0:
        # 직각 삼각형이 될 수 없으므로 Impossible.를 출력합니다.
        print("Impossible.")
    # result가 0보다 크다면
    else:
        # 직각 삼각형이 될 수 있으므로 result의 값의 제곱근에서 소수점 셋째 자리까지로 값을 바꿔줍니다.
        result = "{:.3f}".format(result ** 0.5)
        # 출력 형식에 맞게 출력합니다.
        print(f"{minus_one} = {result}")
    # 다음 테스트 케이스로 넘어 갈 때 한 줄을 더 띄웁니다.
    print()
    # 테스트 케이스의 번호에 1을 더해줍니다.
    idx += 1