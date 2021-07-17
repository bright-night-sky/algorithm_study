# https://programmers.co.kr/learn/courses/30/lessons/12939

# 둘 이상의 정수가 공백으로 구분되어 있는 문자열 s가 매개변수로 주어집니다.
def solution(s):
    # 문자열 s를 공백으로 구분한 뒤, 각 숫자를 정수형으로 변환하고 리스트 변수에 넣어줍니다.
    nums = list(map(int, s.split(' ')))
    # 반환 형식에 맞게 최솟값과 최댓값을 저장하는 문자열 변수를 선언합니다.
    max_min = f'{min(nums)} {max(nums)}'

    # max_min의 값을 반환합니다.
    return max_min