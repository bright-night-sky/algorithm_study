# https://programmers.co.kr/learn/courses/30/lessons/12950

# 2개의 행렬 arr1, arr2가 매개변수로 주어집니다.
def solution(arr1, arr2):
    # 두 행렬 arr1과 arr2의 덧셈 결과를 저장할 변수를 선언합니다.
    answer = []
    # 행렬에서 열의 길이를 저장하는 변수를 선언합니다.
    col_len = len(arr1)
    # 행렬에서 행의 길이를 저장하는 변수를 선언합니다.
    row_len = len(arr1[0])

    # 열의 길이만큼 반복합니다.
    for i in range(col_len):
        # 현재 열 인덱스에서 행의 덧셈 결과를 저장할 리스트 변수를 선언합니다.
        answer_row = []

        # 현재 열에서 행의 길이만큼 반복합니다.
        for j in range(row_len):
            # 현재 행, 열의 인덱스에서의 arr1과 arr2의 원소의 덧셈을 구하고 answer_row에 넣어줍니다.
            answer_row.append(arr1[i][j] + arr2[i][j])

        # 한 행의 덧셈이 끝나면 행 자체를 answer에 넣어줍니다.
        answer.append(answer_row)

    # 행렬의 덧셈 결과를 반환합니다.
    return answer