# https://www.acmicpc.net/problem/5354

# 첫째 줄에 테스트 케이스의 개수 입력
test_cases = int(input())

# 테스트 케이스만큼 반복문 실행
for case in range(0, test_cases):
    # J박스 크기 출력
    Jbox_size = int(input())

    # 현재 J박스의 각 열마다 출력
    for row in range(0, Jbox_size):
        # 만약 J박스의 첫 번째 열이거나 마지막 열인 경우
        if row == 0 or row == (Jbox_size - 1):
            # #만 여러 개 있는 열 출력
            print('#' * Jbox_size)
        # J박스의 중간에 있는 열이라면
        else:
            # 중간에 J도 들어간 형태로 출력
            print('#', end='')
            print('J' * (Jbox_size - 2), end='')
            print('#')
    # 박스와 박스 사이에는 빈 줄 하나 출력
    print()