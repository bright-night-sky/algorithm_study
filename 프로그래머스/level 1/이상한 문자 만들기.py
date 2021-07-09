# https://programmers.co.kr/learn/courses/30/lessons/12930

# 한 개 이상의 단어로 구성되어 있는 문자열 s가 매개변수로 주어집니다.
def solution(s):
    # 변환된 단어들이 저장될 리스트 변수를 선언합니다.
    answer = []
    # 문자열 s를 공백으로 구분한 단어들을 저장한 리스트 변수를 선언합니다.
    words = s.split(' ')

    # words의 한 단어씩 반복해봅니다.
    for word in words:
        # 현재 단어가 변환된 단어를 저장할 변수를 선언합니다.
        changed_word = ''
        # 현재 단어의 길이를 저장하는 변수를 선언합니다.
        word_len = len(word)

        # 현재 단어의 길이만큼 반복합니다.
        for idx in range(word_len):
            # 단어의 현재 인덱스가 홀수 번째라면
            if idx % 2 == 0:
                # 현재 인덱스의 글자를 대문자로 변경해 changed_word에 넣어줍니다.
                changed_word += word[idx].upper()
            # 단어의 현재 인덱스가 짝수 번째라면
            else:
                # 현재 인덱스의 글자를 소문자로 변경해 changed_word에 넣어줍니다.
                changed_word += word[idx].lower()

        # 변환된 단어 changed_word를 answer에 넣어줍니다.
        answer.append(changed_word)

    # answer에 있는 변환된 단어들을 사이마다 공백을 넣어 문자열로 만들어줍니다.
    answer = ' '.join(answer)

    # 변환된 최종 결과를 반환합니다.
    return answer