# https://www.acmicpc.net/problem/20001

# 첫 번째 줄에 "고무오리 디버깅 시작"이라고 입력합니다.
start = input()

# 문제의 개수를 저장하는 변수를 선언합니다.
question = 0

# "고무오리 디버깅 끝"을 입력할 때까지 반복합니다.
while True:
    # 문제, 고무오리 혹은 고무오리 디버깅 끝을 입력합니다.
    is_rubberduck = input()

    # 고무오리 디버깅 끝을 입력했다면
    if is_rubberduck == "고무오리 디버깅 끝":
        # 반복문을 탈출합니다.
        break
    # 문제 혹은 고무오리를 입력했다면
    else:
        # 문제를 입력했다면
        if is_rubberduck == "문제":
            # 문제의 개수에 1을 더해줍니다.
            question += 1
        # 고무오리를 입력했다면
        elif is_rubberduck == "고무오리":
            # 문제의 개수가 0개인 경우
            if question == 0:
                # 체벌로 문제의 개수에 2를 더해줍니다.
                question += 2
            # 문제의 개수가 1개 이상인 경우
            else:
                # 한 문제를 해결하므로 문제의 개수에서 1을 뺍니다.
                question -= 1

# 남은 문제의 개수가 0개라면
if question == 0:
    # 고무오리야 사랑해를 출력합니다.
    print("고무오리야 사랑해")
# 남은 문제의 개수가 1개 이상이라면
else:
    # 힝구를 출력합니다.
    print("힝구")
