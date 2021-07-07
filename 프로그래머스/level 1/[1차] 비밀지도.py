# https://programmers.co.kr/learn/courses/30/lessons/17681

# 지도의 한 변 크기 n, 지도 2개의 정보를 저장한 리스트 arr1, arr2가 매개변수로 주어집니다.
def solution(n, arr1, arr2):
    # 원래의 비밀지도를 해독한 정보를 저장할 리스트 변수를 선언합니다.
    answer = [None] * n

    # 지도의 한 변의 크기 n만큼 반복합니다.
    for idx in range(n):
        # 원래 비밀지도의 현재의 한 줄을 해독한 결과를 저장하는 변수를 선언합니다.
        arr_sharp = ''
        # 두 비밀지도의 현재의 한 줄을 or 연산하고 이진수로 바꾼 후
        # 앞의 0b를 떼어준 결과를 저장하는 변수를 선언합니다.
        arr_bin = bin(arr1[idx] | arr2[idx])[2:]

        # 만약 arr_bin의 길이가 지도의 한 변 크기인 n과 다르다면
        if len(arr_bin) != n:
            # arr_bin에서 n보다 모자란 길이만큼 앞에 0을 붙여줍니다.
            arr_bin = '0' * (n - len(arr_bin)) + arr_bin

        # arr_bin에서 한 글자씩 반복합니다.
        for char in arr_bin:
            # 현재 글자가 1이라면
            if char == '1':
                # arr_sharp에 #을 넣어줍니다.
                arr_sharp += '#'
            # 현재 글자가 0이라면
            elif char == '0':
                # arr_sharp에 공백을 넣어줍니다.
                arr_sharp += ' '

        # answer에 현재 해독한 한 줄의 정보를 넣어줍니다.
        answer[idx] = arr_sharp

    # 원래의 비밀지도를 해독한 정보를 반환합니다.
    return answer