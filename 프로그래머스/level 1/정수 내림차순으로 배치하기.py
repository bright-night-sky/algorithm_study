# https://programmers.co.kr/learn/courses/30/lessons/12933

# 정수 n이 매개변수로 주어집니다.
# 1 이상 8,000,000,000 이하인 자연수입니다.
def solution(n):
    # n을 각 자리수를 문자열로 만들고 리스트에 넣어준 뒤, 내림차순으로 정렬합니다.
    # 내림차순된 리스트 값들을 다시 문자열로 만들고 정수로 변환한 뒤, answer 변수에 저장합니다.
    answer = int(''.join(sorted(list(str(n)), reverse=True)))

    # answer의 값을 반환합니다.
    return answer