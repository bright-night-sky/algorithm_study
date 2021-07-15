# https://programmers.co.kr/learn/courses/30/lessons/1845

# N마리의 폰켓몬의 종류 번호가 담긴 리스트 nums가 매개변수로 주어집니다.
# 길이 N은 1 이상 10,000 이하의 자연수이고, 항상 짝수입니다.
# 폰켓몬의 종류 번호는 1 이상 200,000 이하의 자연수입니다.
def solution(nums):
    # 서로 다른 폰켓몬 종류의 개수를 저장하는 변수를 선언합니다.
    different_cnt = len(set(nums))
    # 선택하는 폰켓몬의 수를 저장하는 변수를 선언합니다.
    choice = len(nums) // 2

    # 선택하는 폰켓몬 수가 서로 다른 폰켓몬 종류의 개수보다 크다면
    if choice > different_cnt:
        # answer에 different_cnt를 저장합니다.
        answer = different_cnt
    # 선택하는 폰켓몬 수가 서로 다른 폰켓몬 종류의 개수보다 작거나 같다면
    else:
        # answer에 choice를 저장합니다.
        answer = choice

    # answer의 값을 반환합니다.
    return answer