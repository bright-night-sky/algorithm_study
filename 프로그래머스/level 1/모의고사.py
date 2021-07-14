# https://programmers.co.kr/learn/courses/30/lessons/42840

# 시험 문제의 정답이 있는 리스트 answer가 매개변수로 주어집니다.
# 최대 10,000 문제이고, 정답은 1 ~ 5 중 하나입니다.
def solution(answers):
    # 가장 높은 점수를 받은 사람들의 번호를 저장할 리스트 변수를 선언합니다.
    answer = []
    # answers의 길이를 저장하는 변수를 선언합니다.
    answers_len = len(answers)
    # 1번 수포자의 찍는 방식을 저장한 튜플 변수를 선언합니다.
    first = (1, 2, 3, 4, 5)
    # 2번 수포자의 찍는 방식을 저장한 튜플 변수를 선언합니다.
    second = (2, 1, 2, 3, 2, 4, 2, 5)
    # 3번 수포자의 찍는 방식을 저장한 튜플 변수를 선언합니다.
    third = (3, 3, 1, 1, 2, 2, 4, 4, 5, 5)
    # 1번, 2번, 3번 수포자들의 찍는 방식의 길이를 저장한 변수들을 선언합니다.
    first_len = 5
    second_len = 8
    third_len = 10
    # 1번, 2번, 3번 수포자들이 맞은 문제의 개수를 저장할 리스트 변수를 선언합니다.
    corrects = [0] * 3

    # 시험의 각 문제마다 반복해봅니다.
    for idx in range(answers_len):
        # 현재 문제의 정답과 1번 수포자가 찍는 방식이 일치한다면
        if answers[idx] == first[idx % first_len]:
            # corrects의 첫 번째 인덱스에 1을 더해줍니다.
            corrects[0] += 1

        # 현재 문제의 정답과 2번 수포자가 찍는 방식이 일치한다면
        if answers[idx] == second[idx % second_len]:
            # corrects의 두 번째 인덱스에 1을 더해줍니다.
            corrects[1] += 1

        # 현재 문제의 정답과 3번 수포자가 찍는 방식이 일치한다면
        if answers[idx] == third[idx % third_len]:
            # corrects의 세 번째 인덱스에 1을 더해줍니다.
            corrects[2] += 1

    # 1번, 2번, 3번 수포자들이 맞은 문제의 개수 중 가장 많이 맞은 개수를 저장하는 변수를 선언합니다.
    max_correct = max(corrects)

    # 1번, 2번, 3번 수포자들이 맞은 문제 개수를 반복해봅니다.
    for idx in range(3):
        # 현재 수포자가 맞은 문제 개수와 가장 많이 맞은 개수가 같다면
        if corrects[idx] == max_correct:
            # answer에 현재 수포자의 번호를 넣어줍니다.
            answer.append(idx + 1)

    # 가장 많은 문제를 맞힌 수포자의 번호들을 저장한 answer를 반환합니다.
    return answer