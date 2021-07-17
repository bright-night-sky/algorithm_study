# https://programmers.co.kr/learn/courses/30/lessons/12951

# 문자열 s가 매개변수로 주어집니다.
# 길이가 1 이상이며, 알파벳과 공백문자(" ")로 이루어져 있습니다.
def solution(s):
    # JadenCase 문자열 결과를 저장할 변수를 선언합니다.
    result = ''
    # 한 단어를 임시로 저장할 변수를 선언합니다.
    word = ''

    # 문자열 s에서 한 문자씩 반복합니다.
    for char in s:
        # 현재 문자가 공백문자(" ")인 경우
        if char == ' ':
            # word에 문자열이 저장되어 있다면
            if word != '':
                # word의 맨 앞 글자를 대문자로 만들어줍니다.
                word = word[0].upper() + word[1:]
                # word의 값을 result에 넣어줍니다.
                result += word
                # word를 빈 문자열로 만듭니다.
                word = ''

            # result에 공백문자를 넣어줍니다.
            result += ' '
        # 현재 문자가 공백문자가 아니라면
        else:
            # 현재 문자를 소문자로 만들고 word에 넣어줍니다.
            word += char.lower()

    # 반복문이 끝나고 word에 단어가 저장되어 있는 경우
    if word != '':
        # word의 맨 앞 글자를 대문자로 만들어줍니다.
        word = word[0].upper() + word[1:]
        # result에 word의 값을 넣어줍니다.
        result += word

    # JadenCase가 된 문자열을 반환합니다.
    return result