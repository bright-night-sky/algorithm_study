# https://www.acmicpc.net/problem/2511

# A와 B의 카드 순서 입력
A_cards = list(map(int, input().split(' ')))
B_cards = list(map(int, input().split(' ')))

# A와 B가 얻은 총점을 저장하는 변수
A_score = 0
B_score = 0

# 마지막에 이긴 사람을 저장하는 변수
# 모든 라운드에서 비기는 경우도 있기 때문에 초기화를 'D'로 해줬다.
# 라운드에서 이기는 사람을 저장한다.
last_winner = 'D'

# 10라운드 게임 진행
for i in range(0, 10):
    # A의 카드가 더 큰 경우
    if A_cards[i] > B_cards[i]:
        # A에게 3점 추가
        A_score += 3
        # 이긴 사람을 A로 일단 저장
        last_winner = 'A'
    # B의 카드가 더 큰 경우
    elif A_cards[i] < B_cards[i]:
        # B에게 3점 추가
        B_score += 3
        # 이긴 사람을 B로 일단 저장
        last_winner = 'B'
    # A, B의 카드가 동일한 경우
    else:
        # A, B 둘 모두에게 1점 추가
        A_score += 1
        B_score += 1

# 첫 번째 줄에 A, B의 총 승점을 출력
print(A_score, B_score)

# A의 점수가 더 큰 경우 A 승리
if A_score > B_score:
    # A 출력
    print('A')
# B의 점수가 더 큰 경우 B 승리
elif A_score < B_score:
    # B 승리
    print('B')
# A와 B의 점수가 같은 경우
else:
    # 제일 마지막에 이긴 사람이 있는 경우
    if last_winner != 'D':
        # 가장 마지막에 이긴 사람 출력
        print(last_winner)
    # 모든 게임을 비긴 경우
    else:
        # D 출력
        print(last_winner)