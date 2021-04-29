# https://www.acmicpc.net/problem/11256

# 첫 번째 줄에는 테스트 케이스의 개수 T를 입력합니다.
# 1 <= T <= 10
T = int(input())

# 테스트 케이스의 개수 T만큼 반복합니다.
for test_case in range(T):
    # 사탕의 개수 j, 상자의 개수 N을 공백으로 구분해 입력합니다.
    # 1 <= J, N <= 1,000
    J, N = map(int, input().split(' '))

    # 각 상자들의 크기를 저장하는 리스트 변수를 선언합니다.
    boxes = []

    # 상자의 개수 N만큼 반복합니다.
    for box_num in range(N):
        # 이번 상자의 세로 길이 Ri, 가로 길이 Ci를 공백으로 구분해 입력합니다.
        # 1 <= Ri, Ci <= 10,000
        Ri, Ci = map(int, input().split(' '))

        # 세로 길이 * 가로 길이인 상자의 크기를 저장하는 변수를 선언합니다.
        box = Ri * Ci

        # boxes 리스트 변수에 현재 상자의 크기 box의 값을 넣어줍니다.
        boxes.append(box)

    # 가장 큰 상자부터 탐색하기 위해
    # boxes 리스트 변수의 값들을 내림차순으로 정렬합니다.
    boxes.sort(reverse=True)

    # 상자에 담길 수 있는 사탕의 개수를 저장하는 변수를 선언합니다.
    boxed_candies = 0

    # 상자를 하나씩 반복해봅니다.
    for box_index in range(len(boxes)):
        # 상자에 담길 수 있는 사탕의 개수에 현재 상자가 담을 수 있는 사탕의 개수를 더합니다.
        boxed_candies += boxes[box_index]

        # 상자에 담길 수 있는 사탕의 개수가 전체 사탕의 개수보다 크거나 같다면
        if boxed_candies >= J:
            # 현재 상자의 인덱스에 1을 더한 값을 출력합니다.
            print(box_index + 1)
            # 반복문을 탈출합니다.
            break
