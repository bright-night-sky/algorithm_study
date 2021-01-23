# https://www.acmicpc.net/problem/4493

# 테스트 케이스의 개수 t 입력
# 0 < t < 1000
t = int(input())

# 테스트 케이스의 개수만큼 실행
for i in range(0, t):
    # 각 테스트 케이스의 첫째 줄에는 가위 바위 보를 한 횟수 n 입력
    # 0 < n < 100
    n = int(input())

    # Player 1이 이기는 횟수
    player1_win = 0
    # Player 2가 이기는 횟수
    player2_win = 0

    # n번만큼 가위 바위 보를 한다.
    for j in range(0, n):
        # Player 1과 Player 2가 낸 가위 바위 보를 입력
        player1, player2 = input().split(' ')

        # Player 1이 이기는 경우
        # Player 1 : 바위(R) vs Player 2 : 가위(S)
        # Player 1 : 보(P) vs Player 2 : 바위(R)
        # Player 1 : 가위(S) vs Player 2 : 보(P)
        if (player1 == 'R' and player2 == 'S') or (player1 == 'P' and player2 == 'R') or (player1 == 'S' and player2 == 'P'):
            # Player 1의 이긴 횟수에 1 추가
            player1_win += 1
        # Player 2가 이기는 경우
        # Player 1 : 바위(R) vs Player 2 : 보(P)
        # Player 1 : 보(P) vs Player 2 : 가위(S)
        # Player 1 : 가위(S) vs Player 2 : 바위(R)
        elif (player1 == 'R' and player2 == 'P') or (player1 == 'P' and player2 == 'S') or (player1 == 'S' and player2 == 'R'):
            # Player 2의 이긴 횟수에 1 추가
            player2_win += 1
        # Player 1과 Player 2가 비기는 경우
        # Player 1 : 바위(R) vs Player 2 : 바위(R)
        # Player 1 : 보(P) vs Player 2 : 보(P)
        # Player 1 : 가위(S) vs Player 2 : 가위(S)
        else:
            # 그냥 넘어간다.
            continue

    # Player 1의 이긴 횟수가 더 많으면
    if player1_win > player2_win:
        # Player 1 출력
        print("Player 1")
    # Player 2의 이긴 횟수가 더 많으면
    elif player1_win < player2_win:
        # Player 2 출력
        print("Player 2")
    # 이긴 횟수가 같다면
    else:
        # TIE 출력
        print("TIE")
