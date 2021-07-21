# https://programmers.co.kr/learn/courses/30/lessons/12926

# 문자열 s, 거리 n이 매개변수로 주어집니다.
# 문자열 s는 알파벳 소문자, 대문자, 공백으로만 이루어져 있습니다.
# 문자열 s의 길이는 8,000 이하입니다.
# n은 1 이상, 25 이하인 자연수입니다.
def solution(s, n):
    # 소문자 알파벳을 순서대로 저장한 변수를 선언합니다.
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    # 문자열 s를 n만큼 민 암호문을 저장할 변수를 선언합니다.
    cipher = ''

    # 문자열 s에서 한 문자씩 반복해봅니다.
    for char in s:
        # 현재 문자가 공백이라면
        if char == ' ':
            # 공백 그대로를 cipher에 넣어줍니다.
            cipher += char
            # 다음 문자로 넘어갑니다.
            continue

        # 현재 문자가 대문자라면
        if char.isupper():
            # alphabet을 대문자로 변경하고 난 뒤, 현재 문자의 인덱스를 저장하는 변수를 선언합니다.
            char_idx = alphabet.upper().index(char)
        # 현재 문자가 소문자라면
        else:
            # alphabet에서 현재 문자의 인덱스를 저장하는 변수를 선언합니다.
            char_idx = alphabet.index(char)

        # 현재 문자의 alphabet에서의 인덱스에서 거리 n만큼 민 인덱스를 저장하는 변수를 선언합니다.
        cipher_idx = char_idx + n

        # cipher_idx가 26보다 크거나 같다면
        if cipher_idx >= 26:
            # 맨 끝의 z를 초과한 것이므로 26을 빼줍니다.
            cipher_idx -= 26

        # 현재 문자가 대문자라면
        if char.isupper():
            # 현재 문자에서 거리 n만큼 민 알파벳을 대문자로 만들고 cipher에 넣어줍니다.
            cipher += alphabet[cipher_idx].upper()
        # 현재 문자가 소문자라면
        else:
            # 현재 문자에서 거리 n만큼 민 알파벳 소문자를 cipher에 넣어줍니다.
            cipher += alphabet[cipher_idx]

    # 문자열 s를 n만큼 민 암호문을 반환합니다.
    return cipher