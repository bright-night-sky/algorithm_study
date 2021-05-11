# https://www.acmicpc.net/problem/10801

# 첫 번째 줄에는 A가 제시한 카드의 숫자 1부터 10까지 10개를 입력합니다.
# 각 숫자를 정수형으로 변환하고 리스트 변수에 넣어줍니다.
A_cards = list(map(int, input().split(' ')))
# 두 번째 줄에는 B가 제시한 카드의 숫자 1부터 10까지 10개를 입력합니다.
# 각 숫자를 정수형으로 변환하고 리스트 변수에 넣어줍니다.
B_cards = list(map(int, input().split(' ')))

# A가 이긴 횟수를 저장할 변수를 선언합니다.
A_win_count = 0
# B가 이긴 횟수를 저장할 변수를 선언합니다.
B_win_count = 0

# 10라운드를 반복해봅니다.
for round in range(10):
    # 이번 라운드에서 A 카드의 숫자가 B 카드의 숫자보다 크다면
    if A_cards[round] > B_cards[round]:
        # A의 이긴 횟수에 1을 더해줍니다.
        A_win_count += 1
    # 이번 라운드에서 A 카드의 숫자가 B 카드의 숫자보다 작다면
    elif A_cards[round] < B_cards[round]:
        # B의 이긴 횟수에 1을 더해줍니다.
        B_win_count += 1

# A의 이긴 횟수가 B의 이긴 횟수보다 크다면
if A_win_count > B_win_count:
    # A를 출력합니다.
    print('A')
# A의 이긴 횟수가 B의 이긴 횟수보다 작다면
elif A_win_count < B_win_count:
    # B를 출력합니다.
    print('B')
# A, B의 이긴 횟수가 같다면
else:
    # D를 출력합니다.
    print('D')