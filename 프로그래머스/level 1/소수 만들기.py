# https://programmers.co.kr/learn/courses/30/lessons/12977

# combinations를 사용하기 위해 import합니다.
from itertools import combinations


# 숫자들이 들어있는 리스트 nums가 매개변수로 주어집니다.
# 숫자의 개수는 3개 이상 50개 이하입니다.
# 각 원소는 1 이상 1,000 이하의 자연수이고, 중복된 숫자는 없습니다.
def solution(nums):
    # 서로 다른 3개의 숫자를 더해 소수가 되는 경우의 개수를 저장할 변수를 선언합니다.
    answer = 0
    # nums에서 서로 다른 3개의 숫자를 뽑은 경우의 수를 저장한 튜플 변수를 선언합니다.
    three_comb = tuple(combinations(nums, 3))

    # three_comb에서 각 경우의 수를 반복해봅니다.
    for comb in three_comb:
        # 서로 다른 3개의 숫자를 뽑은 현재 경우의 수의 합을 저장하는 변수를 선언합니다.
        comb_sum = sum(comb)
        # comb_sum이 소수인지를 판별하기 위해
        # 1부터 comb_sum의 제곱근까지 반복할 것이므로
        # comb_sum의 제곱근보다 작거나 같은 정수에 1을 더한 수를 저장하는 변수를 선언합니다.
        limit = int(comb_sum ** 0.5) + 1

        # 2부터 limit - 1까지 반복해봅니다.
        for i in range(2, limit):
            # comb_sum이 현재 i로 나누어진다면
            if comb_sum % i == 0:
                # comb_sum은 소수가 아니므로 반복문을 탈출합니다.
                break
        # 반복문을 탈출하지 않는다면
        else:
            # comb_sum은 소수이므로 answer에 1을 더해줍니다.
            answer += 1

    # 소수가 되는 경우의 개수를 반환합니다.
    return answer