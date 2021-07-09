# https://programmers.co.kr/learn/courses/30/lessons/81301

# 숫자의 일부 자릿수가 영단어로 바뀌어졌거나, 혹은 바뀌지 않고 그대로인 문자열 s가 매개변수로 주어집니다.
def solution(s):
    # 문자열 s가 의미하는 원래 숫자를 저장할 변수를 선언합니다.
    answer = ''
    # 각 영단어가 의미하는 숫자를 연결시켜놓은 딕셔너리 변수를 선언합니다.
    eng_num = {
        'zero': '0',
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }
    # 한 숫자 단위의 영단어를 임시로 저장할 변수를 선언합니다.
    temp_eng_num = ''

    # 문자열 s에서 한 글자씩 반복합니다.
    for char in s:
        # 현재 글자가 0에서 9인 숫자 형태의 문자라면
        if ord('0') <= ord(char) <= ord('9'):
            # answer에 숫자 형태인 현재 글자를 넣어줍니다.
            answer += char
        # 현재 글자가 숫자 형태의 문자가 아니라면
        else:
            # temp_eng_num에 현재 글자를 넣어줍니다.
            temp_eng_num += char

            # temp_eng_num이 숫자를 의미하는 영단어라면
            if temp_eng_num in eng_num.keys():
                # 해당 영단어가 의미하는 숫자를 answer에 넣어줍니다.
                answer += eng_num[temp_eng_num]
                # temp_eng_num은 빈 문자열로 만들어줍니다.
                temp_eng_num = ''

    # answer에 저장된 숫자 형태의 문자열을 int형으로 변환합니다.
    answer = int(answer)

    # answer에 저장된 숫자를 반환합니다.
    return answer