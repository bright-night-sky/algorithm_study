# https://programmers.co.kr/learn/courses/30/lessons/12937

# 정수 num이 매개변수로 주어집니다.
# num은 int 범위의 정수입니다.
def solution(num):
    # 정답인 Even이나 Odd를 저장할 변수를 선언합니다.
    answer = ''

    # num이 짝수라면
    if num % 2 == 0:
        # answer에 Even을 저장합니다.
        answer = 'Even'
    # num이 홀수라면
    else:
        # answer에 Odd를 저장합니다.
        answer = 'Odd'

    # answer에 저장된 값을 반환합니다.
    return answer