# https://programmers.co.kr/learn/courses/30/lessons/12918

# 문자열 s가 매개변수로 주어집니다.
def solution(s):
    # 조건에 맞는 문자열인지 아닌지를 저장할 변수를 선언합니다.
    # 처음에는 조건에 맞는 문자열이라는 뜻인 True로 초기화합니다.
    answer = True
    # 문자열 s의 길이를 저장하는 변수를 선언합니다.
    s_len = len(s)

    # 문자열 s의 길이가 4 혹은 6이 아니라면
    if s_len != 4 and s_len != 6:
        # 조건에 맞지 않는 문자열이므로 answer에 False를 저장합니다.
        answer = False
    # 문자열 s의 길이가 4 혹은 6이라면
    else:
        # 문자열 s를 한 글자씩 반복해봅니다.
        for char in s:
            # 현재 글자가 숫자 형태의 문자가 아니라면
            if ord(char) < ord('0') or ord(char) > ord('9'):
                # 조건에 맞지 않는 문자열이므로 answer에 False를 저장합니다.
                answer = False
                # 반복문을 탈출합니다.
                break

    # answer의 값을 반환합니다.
    return answer