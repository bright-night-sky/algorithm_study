# https://www.acmicpc.net/problem/2476

# 참여하는 사람 수 N (2 <= N <= 1000) 입력
N = int(input())
# 최대 상금을 저장하는 변수
max_prize = 0

# 참여하는 사람 수만큼 주사위 세 번씩 던짐
for i in range(0, N):
    # 주사위 3번 던지기
    # 던져서 나온 숫자를 배열에 저장
    dice = list(map(int, input().split(' ')))
    # 현재 주사위를 던지는 사람의 상금을 저장하는 변수
    prize = 0

    # 숫자 1부터 6까지 숫자를 주사위를 던져서 나온 숫자 갯수 세기
    for i in range(1, 7):
        # 주사위를 던져서 나온 숫자 중 1부터 6까지 숫자 개수 세기
        num_count = dice.count(i)

        # 똑같은 숫자가 3개인 경우
        if num_count == 3:
            # 상금 계산
            prize = 10000 + 1000 * i
            # 더 이상 볼 필요 없으므로 break
            break
        # 똑같은 숫자가 2개인 경우
        elif num_count == 2:
            # 상금 계산
            prize = 1000 + 100 * i
            # 더 이상 볼 필요 없으므로
            break
        # 숫자가 1개 이하인 경우
        else:
            # 일단 넘김
            continue

    # prize의 값이 아직 0인 경우는 던진 주사위의 숫자가 모든 다른 경우이다.
    if prize == 0:
        # 상금 계산
        prize = max(dice[0], dice[1], dice[2]) * 100

    # 현재까지의 최대 상금 저장해놓기
    if max_prize < prize:
        max_prize = prize

# 최대 상금 출력하기
print(max_prize)
