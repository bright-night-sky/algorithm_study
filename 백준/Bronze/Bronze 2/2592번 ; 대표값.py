# https://www.acmicpc.net/problem/2592

# readline을 사용하기 위해 import합니다.
from sys import stdin

# 10개의 자연수들을 저장할 리스트 변수를 선언합니다.
# None 10개로 초기화합니다.
numbers = [None] * 10

# 10개의 자연수들을 입력합니다.
for idx in range(10):
    # numbers의 각 인덱스에 입력한 자연수를 넣어줍니다.
    numbers[idx] = int(stdin.readline())

# 10개 자연수의 평균을 저장하는 변수를 선언합니다.
avg = int(sum(numbers) / 10)

# 10개 자연수에서 최빈값의 빈도수를 저장할 변수를 선언합니다.
# 0으로 초기화합니다.
max_cnt = 0
# 10개의 자연수에서 최빈값을 저장할 변수를 선언합니다.
max_cnt_number = None

# 10개의 자연수 하나하나를 반복합니다.
for number in numbers:
    # numbers에서 현재 자연수의 개수를 저장하는 변수를 선언합니다.
    number_cnt = numbers.count(number)

    # 현재 자연수의 개수가 max_cnt의 값보다 크거나 같다면
    if number_cnt >= max_cnt:
        # max_cnt의 값을 현재 자연수의 개수로 저장합니다.
        max_cnt = number_cnt
        # max_cnt_number에 현재 자연수를 저장합니다.
        max_cnt_number = number

# 출력 형식에 맞게 평균과 최빈값을 출력합니다.
print(avg)
print(max_cnt_number)