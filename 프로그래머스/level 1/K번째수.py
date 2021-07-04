# https://programmers.co.kr/learn/courses/30/lessons/42748

# 숫자 배열 array와 i, j, k의 조건들이 들어있는 commands를 매개변수로 주어집니다.
def solution(array, commands):
    # k번째에 있는 수들을 저장할 리스트 변수를 선언합니다.
    answer = []

    # commands에 있는 각 조건들을 하나씩 반복해봅니다.
    for command in commands:
        # i번째 숫자부터 j번째 숫자까지 자르고 정렬했을 때, k번째에 있는 수를 구하는 조건을
        # 각 변수에 할당합니다.
        i, j, k = command
        # array에서 i번째 숫자부터 j번째 숫자까지 자른 것을 저장하는 리스트 변수를 선언합니다.
        slice_array = array[i - 1:j]
        # slice_array를 오름차순 정렬합니다.
        slice_array.sort()
        # 오름차순 정렬된 slice_array에서 k번째 숫자를 저장하는 변수를 선언합니다.
        k_num = slice_array[k - 1]
        # answer에 k_num을 넣어줍니다.
        answer.append(k_num)

    # answer를 반환합니다.
    return answer