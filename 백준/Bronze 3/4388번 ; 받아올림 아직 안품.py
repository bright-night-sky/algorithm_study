# https://www.acmicpc.net/problem/4388

# 0 0을 입력할 때까지 실행
while True:
    # 10자리 이내의 양의 정수 또는 0 입력
    num1, num2 = input().split(' ')

    # 0 0이 입력되었다면
    if num1 == '0' and num2 == '0':
        # 반복문 탈출
        break

    # 받아올림의 횟수를 저장하는 변수
    carry_count = 0
    # 이전의 자릿수에서 받아올림이 생겼는지 판단하는 변수
    prev_carry_flag = False

    # 받아올림은 더 짧은 수의 길이까지만 발생할 수 있다.
    # 입력한 두 수 중 더 짧은 자릿수를 가진 숫자의 길이를 저장하는 변수
    shorter_len = min(len(num1), len(num2))

    # 입력받은 두 숫자의 일의 자리 숫자부터 같은 자리 숫자끼리 더해본다.
    # 두 수 중 더 짧은 숫자까지만 더해본다.
    for idx in range(-1, -shorter_len-1, -1):
        # 이전의 자릿수에서 받아올림이 일어난 경우
        if prev_carry_flag:
            # 두 수의 같은 자리를 합할 때 1도 더 더해줘야한다.
            # 두 수의 같은 자리 숫자의 합이 10 이상인 경우
            if (int(num1[idx]) + int(num2[idx]) + 1) >= 10:
                # 받아올림이 생기므로 받아올림 횟수에 1을 더해주고,
                carry_count += 1
                # 받아올림이 생겼다고 flag 변수에 True를 설정한다.
                prev_carry_flag = True
            # 받아올림이 일어나지 않았다면
            else:
                # 받아올림이 생기지 않았다고 False를 설정한다.
                prev_carry_flag = False
        # 이전의 자릿수에서 받아올림이 일어나지 않은 경우
        else:
            # 두 수의 같은 자리 숫자의 합이 10 이상인 경우
            if (int(num1[idx]) + int(num2[idx])) >= 10:
                # 받아올림이 생기므로 받아올림 횟수에 1을 더해준다.
                carry_count += 1
                # 받아올림이 생겼다고 flag 변수에 True를 설정한다.
                prev_carry_flag = True
            # 받아올림이 일어나지 않았다면
            else:
                # 받아올림이 생기지 않았다고 False를 설정한다.
                prev_carry_flag = False

    # 받아올림 횟수를 출력
    print(carry_count)