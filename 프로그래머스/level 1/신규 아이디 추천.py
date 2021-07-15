# https://programmers.co.kr/learn/courses/30/lessons/72410

# 카카오 아이디 규칙에 맞지 않는 신규 유저의 아이디가 매개변수로 주어집니다.
def solution(new_id):
    # 추천하는 새 아이디에 쓰이지 않는 특수문자들을 저장한 변수를 선언합니다.
    special_char = '~!@#$%^&*()=+[{]}:?,<>/'

    # 1단계 규칙을 구현합니다.
    # 모든 대문자를 대응되는 소문자로 치환합니다.
    new_id = new_id.lower()

    # 2단계 규칙을 구현합니다.
    # 임시로 사용될 빈 문자열 변수를 선언합니다.
    temp = ''
    # new_id에서 한 문자씩 반복해봅니다.
    for char in new_id:
        # 현재 문자가 special_char에 속하지 않는다면
        # 즉, 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 문자라면
        if char not in special_char:
            # 임시 변수 temp에 현재 문자를 넣어줍니다.
            temp += char

    # 3단계 규칙을 구현합니다.
    # new_id에 temp의 첫 문자를 저장합니다.
    new_id = temp[0]
    # temp의 두 번째 문자부터 반복해봅니다.
    for char in temp[1:]:
        # new_id의 마지막 문자와 temp에서 반복 중인 현재 문자 모두 마침표(.)라면
        if new_id[-1] == '.' and char == '.':
            # 그냥 넘어갑니다.
            continue
        # 그 외의 경우라면
        else:
            # new_id에 현재 문자를 넣어줍니다.
            new_id += char

    # 4단계 규칙을 구현합니다.
    # new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
    new_id = new_id.strip('.')

    # 5단계 규칙을 구현합니다.
    # new_id가 빈 문자열이라면
    if new_id == '':
        # new_id에 "a"를 대입합니다.
        new_id = 'a'

    # 6단계 규칙을 구현합니다.
    # new_id의 길이가 16자 이상이라면
    if len(new_id) >= 16:
        # new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
        new_id = new_id[:15]

        # 제거 후 마침표(.)가 new_id 끝에 위치한다면
        if new_id[-1] == '.':
            # 끝에 위치한 마침표(.) 문자를 제거합니다.
            new_id = new_id[:-1]

    # 7단계 규칙을 구현합니다.
    # new_id의 길이가 2자 이하라면
    if len(new_id) <= 2:
        # new_id의 마지막 문자를 저장한 변수를 선언합니다.
        last_char = new_id[-1]
        # new_id의 마지막 문자를 길이가 3이 될 때까지 반복해서 끝에 붙입니다.
        new_id += last_char * (3 - len(new_id))

    # 위의 7단계를 거친 new_id의 값을 반환합니다.
    return new_id