# https://programmers.co.kr/learn/courses/30/lessons/12917

# 문자열 s가 매개변수로 주어집니다.
def solution(s):
    # 문자열 s를 한 글자씩 저장되어 있는 리스트 변수로 만들어줍니다.
    s = list(s)

    # s에 있는 각 문자들을 내림차순으로 정렬합니다.
    s.sort(reverse=True)

    # 리스트 변수 s를 다시 문자열로 만들어줍니다.
    answer = ''.join(s)

    # 내림차순된 문자열을 반환합니다.
    return answer