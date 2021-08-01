# https://programmers.co.kr/learn/courses/30/lessons/12941

# 길이가 같고 자연수들이 저장되어 있는 두 리스트 A, B가 매개변수로 주어집니다.
def solution(A, B):
    # 최종적으로 누적된 최솟값을 저장할 변수를 선언합니다.
    min_result = 0
    # A 내부의 값들을 오름차순으로 정렬합니다.
    A.sort()
    # B 내부의 값들을 내림차순으로 정렬합니다.
    B.sort(reverse=True)
    # A의 길이를 저장하는 변수를 선언합니다.
    A_len = len(A)

    # 최종적으로 누적된 최솟값을 구하려면
    # A에서는 작은 값부터 큰 값으로, B에서는 큰 값부터 작은 값으로
    # A, B의 같은 인덱스에 있는 값들을 곱하고 min_result에 더하면 됩니다.
    # 리스트의 인덱스를 반복해봅니다.
    for idx in range(A_len):
        # 현재 인덱스에서의 A와 B의 값을 곱하고 min_result에 더해줍니다.
        min_result += A[idx] * B[idx]

    # 최종적으로 누적된 최솟값을 반환합니다.
    return min_result