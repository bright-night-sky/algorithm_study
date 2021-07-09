# https://programmers.co.kr/learn/courses/30/lessons/12915

# 문자열로 구성된 리스트 strings, 정렬 기준이 될 정수 n이 매개변수로 주어집니다.
def solution(strings, n):
    # strings에 있는 문자열들을 각 문자열의 인덱스 n번째 글자를 기준으로 오름차순 정렬합니다.
    # 인덱스 n번째의 문자가 같은 문자열이 여럿일 경우 사전순으로 정렬합니다.
    # 결과는 answer 변수에 저장합니다.
    answer = sorted(strings, key=lambda string: (string[n], string))

    # answer에 저장되어 있는 정렬이 된 문자열 리스트를 반환합니다.
    return answer