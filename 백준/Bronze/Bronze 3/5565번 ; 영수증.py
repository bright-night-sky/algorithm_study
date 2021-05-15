# https://www.acmicpc.net/problem/5565

# readline을 사용하기 위해 import합니다.
from sys import stdin

# 책 10권의 총 가격을 입력합니다.
# 정수형으로 변환해서 변수에 저장합니다.
total_price = int(stdin.readline())

# 책 9권의 총 가격을 저장할 변수를 선언합니다.
nine_books_price = 0

# 9권의 책을 반복해봅니다.
for _ in range(9):
    # 책 한 권의 가격을 입력하고 정수형으로 변환한 뒤
    # nine_books_price에 더해줍니다.
    # 책의 가격은 10,000 이하인 양의 정수입니다.
    nine_books_price += int(stdin.readline())

# total_price에서 nine_books_price의 값을 빼
# 가격을 읽을 수 없는 책의 가격을 출력합니다.
print(total_price - nine_books_price)