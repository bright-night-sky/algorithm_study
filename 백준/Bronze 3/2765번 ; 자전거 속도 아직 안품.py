# https://www.acmicpc.net/problem/2765

# 출력문의 N을 저장하는 변수입니다.
N = 1

# 회전수를 0으로 입력할 때까지 계속 테스트 케이스를 입력합니다.
while True:
    # 지름, 회전수, 시간을 공백으로 구분하여 입력합니다.
    diameter, rpm, time = input().split(' ')

    # 만약 회전수를 0으로 입력하면
    if rpm == 0:
        # 반복문을 끝냅니다.
        break



    # 결과를 출력합니다.
    print(f"Trip #{N}: {} {}")