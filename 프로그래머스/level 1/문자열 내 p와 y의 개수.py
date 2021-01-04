# https://programmers.co.kr/learn/courses/30/lessons/12916

def solution(s):
    answer = True
    s = s.lower()
    p_count = s.count('p')
    y_count = s.count('y')

    if p_count != y_count:
        answer = False
    else:
        answer = True

    return answer