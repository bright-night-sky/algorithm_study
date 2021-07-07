# https://programmers.co.kr/learn/courses/30/lessons/12919

# String형 배열 seoul이 매개변수로 주어집니다.
def solution(seoul):
    # seoul에서 Kim의 인덱스를 저장하는 변수를 선언합니다.
    Kim_position = seoul.index('Kim')
    # 반환 형식에 맞게 answer의 값을 저장합니다.
    answer = f'김서방은 {Kim_position}에 있다'

    # answer를 반환합니다.
    return answer