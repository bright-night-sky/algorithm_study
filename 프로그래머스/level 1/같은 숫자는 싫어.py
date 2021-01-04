# https://programmers.co.kr/learn/courses/30/lessons/12906

def solution(arr):
    answer = []
    answer.append(arr[0])

    for idx in range(1, len(arr)):
        if arr[idx] == answer[-1]:
            continue
        else:
            answer.append(arr[idx])

    return answer