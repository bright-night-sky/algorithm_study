# https://programmers.co.kr/learn/courses/30/lessons/12948

# 전화번호 문자열인 phone_number가 매개변수로 주어집니다.
# 길이는 4 이상, 20 이하입니다.
def solution(phone_number):
    # 전화번호의 뒷 4자리를 제외한 나머지 숫자를 전부 *로 가린 정답을 저장할 변수를 선언합니다.
    answer = ''
    # phone_number의 길이를 저장하는 변수를 선언합니다.
    phone_len = len(phone_number)

    # answer에 phone_len에서 4를 뺀만큼 *을 넣고, phone_number의 뒷 4자리도 넣어줍니다.
    answer += '*' * (phone_len - 4) + phone_number[-4:]

    # answer의 값을 반환합니다.
    return answer