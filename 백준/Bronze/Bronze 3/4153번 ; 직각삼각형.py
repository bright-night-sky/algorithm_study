# https://www.acmicpc.net/problem/4153

# 0 0 0을 입력할 때까지 실행
while True:
    # 각 변의 길이를 입력하고 리스트 변수에 저장
    # 30,000보다 작은 양의 정수
    sides = list(map(int, input().split(' ')))
    # 리스트 내부의 값을 오름차순으로 정렬
    sides = sorted(sides)

    # 0 0 0을 입력했다면
    if sides[0] == sides[1] == sides[2] == 0:
        # 반복문 탈출
        break
    # 각 변의 길이를 제대로 입력했다면
    else:
        # 피타고라스 공식에 부합해서 직각삼각형이 맞다면
        if sides[2] ** 2 == sides[0] ** 2 + sides[1] ** 2:
            # right 출력
            print("right")
        # 직각삼각형이 아니라면
        else:
            # wrong 출력
            print("wrong")