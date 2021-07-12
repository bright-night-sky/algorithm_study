# https://programmers.co.kr/learn/courses/30/lessons/64061

# 게임 화면의 격자의 상태가 담긴 2차원 리스트 board,
# 인형을 집기 위해 크레인을 작동시킨 위치가 담긴 리스트 moves가 매개변수로 주어집니다.
# board의 2차원 크기는 5 x 5 이상 30 x 30 이하입니다.
# board의 각 칸에는 0 이상 100 이하의 정수가 저장되어 있습니다.
# moves의 길이는 1 이상 1,000 이하입니다.
# moves의 각 원소들의 값은 1 이상이며 board 리스트의 가로 크기 이하인 자연수입니다.
def solution(board, moves):
    # 사라진 인형의 개수를 저장할 변수를 선언합니다.
    answer = 0
    # 크레인이 집은 인형을 넣는 바구니인 리스트 변수를 선언합니다.
    bucket = []

    # moves의 크레인을 작동시킨 위치를 하나씩 반복해봅니다.
    for position in moves:
        # 크레인의 위치에서 board에서 위에서부터 가로 한 줄씩 반복해봅니다.
        for line in board:
            # 크레인의 위치에서 현재 가로줄에서의 인형을 저장하는 변수를 선언합니다.
            doll = line[position - 1]

            # 만약 인형이 0이 아니라면
            if doll != 0:
                # 크레인이 실제로 인형을 집은 것이므로 집은 인형을 bucket에 넣어줍니다.
                bucket.append(doll)
                # 집은 인형은 바구니에 넣었으므로 원래 위치에는 0을 저장합니다.
                line[position - 1] = 0
                # 인형을 넣었으므로 반복문을 탈출합니다.
                break

        # 바구니에 담긴 인형들 중 맨 위의 두 인형이 같은 경우 시도해봅니다.
        try:
            # 바구니에 담긴 인형들 중 맨 위의 두 인형이 같다면
            if bucket[-1] == bucket[-2]:
                # 맨 위의 두 인형을 제거해줍니다.
                bucket.pop()
                bucket.pop()
                # 인형 2개가 사라졌으므로 answer에 2를 더해줍니다.
                answer += 2
        # 바구니에 인형이 하나인 경우에 위와 같은 처리를 하면
        # 오류가 발생할 수 있으므로 예외 처리를 해줍니다.
        except:
            # 아무것도 하지 않습니다.
            pass

    # 사라진 인형의 개수를 반환합니다.
    return answer