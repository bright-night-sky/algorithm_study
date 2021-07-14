# https://programmers.co.kr/learn/courses/30/lessons/77484

# 민우가 구매한 로또 번호를 담은 리스트 lottos, 당첨 번호를 담은 리스트 win_nums가 매개변수로 주어집니다.
# lottos, win_nums 모두 길이가 6인 정수 리스트입니다.
# lottos의 모든 원소는 0 이상 45 이하인 정수입니다.
# win_nums의 모든 원소는 1 이상 45 이하인 정수입니다.
def solution(lottos, win_nums):
    # 맞은 번호의 개수에 따른 로또의 순위를 키-값으로 저장한 딕셔너리 변수를 선언합니다.
    correct_cnt_rank = {
        6: 1,
        5: 2,
        4: 3,
        3: 4,
        2: 5,
        1: 6,
        0: 6
    }
    # lottos에서 0의 개수를 저장하는 변수를 선언합니다.
    zero_cnt = lottos.count(0)
    # lottos의 숫자들 중에서 win_nums에 있는 숫자와 일치하는 것의 개수를 저장할 변수를 선언합니다.
    cur_correct_cnt = 0

    # lottos의 숫자를 하나씩 반복합니다.
    for num in lottos:
        # 현재 숫자가 win_nums에 있다면
        if num in win_nums:
            # cur_correct_cnt에 1을 더해줍니다.
            cur_correct_cnt += 1

    # 가장 많은 번호를 맞춘 경우는 lottos에서 0 외의 숫자가 win_nums의 숫자와 일치한 것의 개수와
    # 알아볼 수 없는 번호 0도 win_nums에 있는 숫자와 일치하는 경우입니다.
    # 가장 많은 번호를 맞췄을 때의 맞춘 개수를 저장하는 변수를 선언합니다.
    max_correct_cnt = cur_correct_cnt + zero_cnt
    # 가장 많은 번호를 맞췄을 때의 순위를 저장하는 변수를 선언합니다.
    max_rank = correct_cnt_rank[max_correct_cnt]
    # 가장 적은 번호를 맞췄을 때의 경우는 알아볼 수 없는 번호 0은 다 빗나간 경우이므로
    # 0 외의 숫자가 win_nums의 숫자와 일치한 것의 개수만 세면 됩니다.
    # 가장 적은 번호를 맞췄을 때의 순위를 저장하는 변수를 선언합니다.
    min_rank = correct_cnt_rank[cur_correct_cnt]

    # 최고 순위와 최저 순위를 저장한 리스트 변수를 선언합니다.
    answer = [max_rank, min_rank]

    # answer를 반환합니다.
    return answer