# https://programmers.co.kr/learn/courses/30/lessons/12935

# 정수를 저장한 리스트 arr이 매개변수로 주어집니다.
# arr은 길이 1 이상인 리스트입니다.
def solution(arr):
    # 정답을 저장할 변수를 선언합니다.
    answer = None
    # 정수를 저장한 리스트 arr에서 가장 작은 수를 저장하는 변수를 선언합니다.
    min_num = min(arr)
    # arr에서 가장 작은 수의 인덱스를 저장하는 변수를 선언합니다.
    min_num_idx = arr.index(min_num)

    # arr에서 가장 작은 수를 제거합니다.
    del arr[min_num_idx]

    # arr이 빈 리스트라면
    if arr == []:
        # answer에 [-1]을 저장합니다.
        answer = [-1]
    # arr이 빈 리스트가 아니라면
    else:
        # 가장 작은 수가 제거된 arr을 answer에 저장합니다.
        answer = arr

    # answer에 저장된 리스트를 반환합니다.
    return answer