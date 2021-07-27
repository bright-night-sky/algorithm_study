# https://programmers.co.kr/learn/courses/30/lessons/60057

# 압축할 문자열 s가 매개변수로 주어집니다.
# s의 길이는 1 이상 1,000 이하입니다.
# s는 알파벳 소문자로만 이루어져 있습니다.
def solution(s):
    # 압축 문자열 중 가장 짧은 길이를 저장할 변수를 선언합니다.
    shortest_len = None
    # 문자열 s의 길이를 저장하는 변수를 선언합니다.
    s_len = len(s)
    # 문자열을 압축할 때, 자를 단위 길이는 한 글자부터 시작하므로, 시작하는 단위 길이를 저장하는 변수를 선언합니다.
    unit_start = 1
    # 문자열을 압축할 때, 자를 단위 길이 중 최대 길이를 저장하는 변수를 선언합니다.
    # 자를 단위는 1부터 문자열 s의 길이의 절반까지 반복할 것이므로 s의 길이의 절반에 1을 더한 값을 저장하는 변수를 선언합니다.
    unit_end = s_len // 2 + 1

    # 문자열 s의 길이가 1이라면
    if s_len == 1:
        # 압축할 필요가 없으므로 가장 짧은 길이가 1입니다.
        shortest_len = 1
    # 문자열 s의 길이가 1보다 크다면
    else:
        # 자를 단위를 1부터 문자열 s의 길이의 절반까지 반복해봅니다.
        for unit in range(unit_start, unit_end):
            # 현재 자를 단위로 압축한 문자열을 저장할 변수를 선언합니다.
            cur_comp_result = ''
            # 문자열 s를 현재 자를 단위로 자른 뒤, 각 문자열을 차례로 반복해볼 때
            # 바로 이전의 압축한 글자 단위를 저장하는 변수를 선언합니다.
            # 처음에는 맨 앞 글자 단위로 초기화합니다.
            cur_comp_unit = s[:unit]
            # 현재 자를 단위로 압축한 글자 단위가 나타나는 횟수를 저장할 변수를 선언합니다.
            # 1번은 나타나므로 1로 초기화합니다.
            repeat_cnt = 1

            # 문자열 s를 unit 값의 인덱스부터 끝까지 현재 자를 단위로 잘라서 잘린 문자열들을 반복해봅니다.
            for idx in range(unit, s_len, unit):
                # 잘린 문자열들 중 현재 반복 중인 문자열을 저장하는 변수를 선언합니다.
                cur_char = s[idx:idx + unit]

                # 바로 이전의 압축한 글자 단위와 현재 반복 중인 문자열이 같다면
                if cur_comp_unit == cur_char:
                    # 압축 횟수에 1을 더해줍니다.
                    repeat_cnt += 1
                # 바로 이전의 압축한 글자 단위와 현재 반복 중인 문자열이 다를 때
                elif cur_comp_unit != cur_char:
                    # 압축 횟수가 1보다 크다면
                    if repeat_cnt > 1:
                        # cur_comp_result에 문자열로 변환한 압축 횟수를 넣어줍니다.
                        cur_comp_result += str(repeat_cnt)

                    # cur_comp_result에 바로 이전의 압축한 글자 단위를 넣어줍니다.
                    cur_comp_result += cur_comp_unit
                    # cur_comp_unit에 현재 반복 중인 문자열을 저장합니다.
                    cur_comp_unit = cur_char
                    # 다른 문자열이 나왔으므로 압축 횟수는 1로 만들어줍니다.
                    repeat_cnt = 1

            # 반복문을 다 돌고 나서 cur_comp_result와 repeat_cnt에 남은 값도 cur_comp_result에 넣어줘야합니다.
            # 압축 횟수가 1보다 크다면
            if repeat_cnt > 1:
                # cur_comp_result에 문자열로 변환한 압축 횟수를 넣어줍니다.
                cur_comp_result += str(repeat_cnt)

            # cur_comp_result에 바로 이전의 압축한 글자 단위를 넣어줍니다.
            cur_comp_result += cur_comp_unit

            # 현재 자를 단위로 압축한 문자열의 길이를 저장하는 변수를 선언합니다.
            cur_comp_len = len(cur_comp_result)

            # 아직 가장 짧은 것의 길이를 구하지 않았거나,
            # 앞서 구한 가장 짧은 것의 길이보다 현재 자를 단위로 압축한 문자열의 길이가 더 짧다면
            if shortest_len == None or cur_comp_len < shortest_len:
                # shortest_len에 현재 자를 단위로 압축한 문자열의 길이를 저장합니다.
                shortest_len = cur_comp_len

    # 압축한 문자열 중 가장 짧은 것의 길이를 반환합니다.
    return shortest_len