# https://www.acmicpc.net/problem/5568

# readline을 사용하기 위해 import합니다.
from sys import stdin
# permutations를 사용하기 위해 import합니다.
from itertools import permutations


# 첫째 줄에 카드의 개수 n을 입력합니다.
# 정수형으로 변환합니다.
n = int(stdin.readline())
# 둘째 줄에 선택하는 카드의 수 k를 입력합니다.
# 정수형으로 변환합니다.
k = int(stdin.readline())
# 카드들에 쓰여있는 수를 저장할 리스트 변수를 선언합니다.
cards = [None] * n

# 카드의 개수 n만큼 반복합니다.
for card_idx in range(n):
    # 카드에 적혀있는 수를 입력합니다.
    # 맨 끝의 \n은 떼어내고 cards에 넣어줍니다.
    cards[card_idx] = stdin.readline().rstrip()

# 카드를 k개 뽑아서 순서대로 나열해본 경우들을 리스트 변수로 선언합니다.
card_pers = list(permutations(cards, k))
# 튜플로 만들어져 있는 card_pers의 값 하나하나들을 숫자로 된 문자열로 만들어 준 후,
# set 변수에 넣어 중복되는 것은 지워줍니다.
numbers = set(map(''.join, card_pers))

# numbers의 길이인 상근이가 만들 수 있는 정수의 개수를 출력합니다.
print(len(numbers))