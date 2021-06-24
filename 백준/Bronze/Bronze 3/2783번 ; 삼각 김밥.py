# https://www.acmicpc.net/problem/2783

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 첫째 줄에 세븐25의 삼각 김밥 가격 정보인 Y그램 당 X원을 공백으로 구분해 입력합니다.
# 1 <= X <= 100
# 1 <= Y <= 1,000
# 각각 정수형으로 변환합니다.
X, Y = map(int, stdin.readline().split(' '))
# 둘째 줄에는 세븐25를 제외한 편의점의 개수 N을 입력합니다.
# 1 <= N <= 100
# 정수형으로 변환합니다.
N = int(stdin.readline())
# 삼각 김밥 1,000그램 가격의 최저가를 저장할 변수를 선언합니다.
# 세븐25의 삼각 김밥의 1,000그램 가격으로 초기화합니다.
lowest_price = X * 1000 / Y

# 편의점의 개수 N개만큼 반복합니다.
for store_idx in range(N):
    # i번째 편의점의 삼각 김밥 가격 정보 Yi그램 당 Xi원을 공백으로 구분해 입력합니다.
    # 1 <= Xi <= 100
    # 1 <= Yi <= 1,000
    # 각각 정수형으로 변환합니다.
    Xi, Yi = map(int, stdin.readline().split(' '))
    # i번째 편의점의 삼각 김밥 1,000그램 가격을 저장하는 변수를 선언합니다.
    unit_price = Xi * 1000 / Yi

    # 이번 편의점의 삼각 김밥 1,000그램 가격이 이전까지의 삼각 김밥 1,000그램 최저 가격보다 작다면
    if lowest_price > unit_price:
        # 삼각 김밥 1,000그램 최저 가격 변수에 이번 편의점의 삼각 김밥 1,000그램 가격을 저장합니다.
        lowest_price = unit_price

# 삼각 김밥 1,000그램 가격의 최저가의 소수점 둘째 자리까지 출력합니다.
print('%.2f' % lowest_price)