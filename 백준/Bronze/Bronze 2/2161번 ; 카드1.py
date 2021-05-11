# https://www.acmicpc.net/problem/2161

# 첫째 줄에 정수 N을 입력합니다.
# 1 <= N <= 1,000
N = int(input())

# 리스트 변수를 선언해 1부터 N까지의 번호가 붙어 있는 카드를 넣어줍니다.
deck = [str(card) for card in range(1, N + 1)]

# 버린 카드들을 차례대로 저장하는 리스트 변수를 선언합니다.
dump = []

# 카드가 한 장 남을 때까지 반복합니다.
while True:
    # 카드가 한 장만 남았다면
    if len(deck) == 1:
        # 남은 카드 한 장도 버리는 카드 변수에 넣어줍니다.
        dump.append(deck[0])
        # 반복문을 탈출합니다.
        break

    # 카드들에서 맨 위에 있는 카드를 버리는 카드 변수에 넣어줍니다.
    dump.append(deck[0])
    deck.pop(0)

    # 그 다음에 있는 카드를 카드 뭉치 맨 아래에 넣어줍니다.
    temp_card = deck[0]
    deck.pop(0)
    deck.append(temp_card)

# 버린 카드 리스트 변수에 있는 값들을 공백으로 구분해 출력합니다.
print(' '.join(dump))