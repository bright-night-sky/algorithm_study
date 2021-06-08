# https://www.acmicpc.net/problem/1302

# readline을 사용하기 위해 import합니다.
from sys import stdin

# 첫째 줄에 오늘 하루 동안 팔린 책의 개수 N을 입력합니다.
# 1,000보다 작거나 같은 자연수입니다.
# 정수형으로 변환합니다.
N = int(stdin.readline())
# 책의 제목을 키, 팔린 책의 개수를 값으로 저장할 딕셔너리 변수를 선언합니다.
books_info = {}

# 오늘 하루 동안 팔린 책의 개수 N만큼 반복합니다.
for book_idx in range(N):
    # 책의 제목을 입력합니다.
    # 맨 끝의 \n은 떼어줍니다.
    book = stdin.readline().rstrip()

    # books_info의 키에 현재 입력한 책의 제목이 없다면
    if book not in books_info.keys():
        # 키를 현재 입력한 책의 제목으로 하고 값을 1로 설정해 books_info에 넣어줍니다.
        books_info[book] = 1
    # books_info의 키에 현재 입력한 책의 제목이 있다면
    else:
        # 해당 책의 제목의 값에 1을 더해줍니다.
        books_info[book] += 1

# books_info의 키-값 튜플을 책이 팔린 개수의 내림차순, 책의 제목의 오름차순으로 정렬합니다.
books_sell = sorted(books_info.items(), key=lambda book: (-book[1], book[0]))

# books_sell의 맨 처음에 있는 책의 정보에서의 책의 이름을 출력합니다.
print(books_sell[0][0])