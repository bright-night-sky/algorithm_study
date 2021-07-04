# https://programmers.co.kr/learn/courses/30/lessons/68644

# 정수 배열 numbers가 주어집니다.
def solution(numbers):
    # 정답을 저장할 리스트 변수를 선언합니다.
    answer = []
    # 정수 배열 numbers의 길이를 저장하는 변수를 선언합니다.
    numbers_len = len(numbers)

    # numbers에서 서로 다른 두 개의 수를 뽑는 반복문을 시작합니다.
    for i in range(numbers_len - 1):
        for j in range(i + 1, numbers_len):
            # 서로 다른 두 개의 수의 합을 저장하는 변수를 선언합니다.
            numbers_sum = numbers[i] + numbers[j]
            # answer에 numbers_sum을 넣어줍니다.
            answer.append(numbers_sum)

    # answer에서 중복되는 값을 없애주기 위해 set로 만들고 다시 리스트 변수로 만들어줍니다.
    answer = list(set(answer))
    # answer 내부의 값들을 오름차순으로 정렬합니다.
    answer.sort()

    # answer을 반환합니다.
    return answer