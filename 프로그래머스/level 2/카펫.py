# https://programmers.co.kr/learn/courses/30/lessons/42842

# Leo가 본 카펫에서 갈색 격자의 수 brown, 노란색 격자의 수 yellow가 매개변수로 주어집니다.
def solution(brown, yellow):
    # 카펫의 가로, 세로 길이를 순서대로 저장할 리스트를 선언합니다.
    carpet = [None, None]

    # 노란색 부분의 세로 길이를 1부터 yellow까지 반복해봅니다.
    for yellow_height in range(1, yellow + 1):
        # yellow 값이 현재 노란색 부분의 세로 길이로 딱 나누어 떨어지지 않는다면
        if yellow % yellow_height != 0:
            # 노란색 부분이 직사각형, 정사각형 모양이 되지 않으므로
            # 다음 세로 길이로 넘어갑니다.
            continue

        # 노란색 부분의 가로 길이를 저장하는 변수를 선언합니다.
        yellow_width = yellow // yellow_height
        # 현재 노란색 부분 가로 길이, 세로 길이의 사각형을 둘러싼 갈색 격자의 수를 저장하는 변수를 선언합니다.
        cur_case_brown = (yellow_height + 2) * 2 + 2 * yellow_width

        # Leo가 본 카펫에서 갈색 격자의 수와 위에서 계산한 갈색 격자의 수가 같다면
        if brown == cur_case_brown:
            # 현재 노란색 부분의 모양이 Leo가 본 카펫과 일치하므로
            # 노란색 부분의 가로 길이와 세로 길이에 각각 2를 더하고 carpet에 넣어줍니다.
            carpet[0] = yellow_width + 2
            carpet[1] = yellow_height + 2
            # 정답을 찾았으므로 반복문을 탈출합니다.
            break

    # Leo가 본 카펫의 가로 길이, 세로 길이 리스트 변수를 반환합니다.
    return carpet