# https://programmers.co.kr/learn/courses/30/lessons/12944

# 정수를 담고 있는 리스트 arr이 매개변수로 주어집니다.
def solution(arr):
    # arr의 모든 정수의 합을 arr의 길이로 나누어 나온 평균을 answer 변수에 저장합니다.
    answer = sum(arr) / len(arr)

    # 평균을 반환합니다.
    return answer