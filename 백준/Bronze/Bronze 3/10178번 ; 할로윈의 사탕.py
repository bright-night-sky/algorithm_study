# https://www.acmicpc.net/problem/10178

# readline을 사용하기 위해 import합니다.
from sys import stdin

# 첫 번째 줄에는 테스트 케이스의 수를 입력합니다.
# 정수형으로 변환해줍니다.
test_case_cnt = int(stdin.readline())

# 테스트 케이스의 수만큼 반복해봅니다.
for _ in range(test_case_cnt):
    # 사탕의 개수 c, 형제의 수 v를 공백으로 구분해 입력합니다.
    # 각각 정수형으로 변환해줍니다.
    c, v = map(int, stdin.readline().split(' '))

    # 형제 한 명이 최대로 받는 사탕의 개수를 저장하는 변수를 선언합니다.
    one_brother_candies = c // v
    # 형제들에게 모두 사탕을 배분하고 난 뒤 아버지에게 남은 사탕의 개수를 저장하는 변수를 선언합니다.
    dad_candies = c - v * one_brother_candies

    # 출력 형식에 맞게 출력합니다.
    print(f"You get {one_brother_candies} piece(s) and your dad gets {dad_candies} piece(s).")