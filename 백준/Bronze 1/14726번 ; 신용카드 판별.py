# https://www.acmicpc.net/problem/14726

# 첫째 줄에 테스트 케이스의 수 T를 입력합니다.
# 1 <= T <= 1000
T = int(input())

# 테스트 케이스의 수 T만큼 반복합니다.
for test_case in range(T):
    # 신용카드의 16자리 숫자를 입력합니다.
    credit_num = input()

    # Luhn 공식을 통해 나오는 합을 저장하는 변수를 선언합니다.
    credit_num_sum = 0

    # 신용카드 16자리 숫자를 하나씩 반복합니다.
    for index in range(0, len(credit_num)):
        # 1번 공식에서의 맨 우측 수부터 세어 짝수 번째라는 말은
        # 맨 좌측 수부터 세어 홀수 번째라는 말과 같습니다.
        # 따라서 좌측 수부터 세어 홀수 번째라면
        if (index+1) % 2 != 0:
            # 2배로 만들어줍니다.
            num = int(credit_num[index]) * 2

            # 2번 공식 내용처럼 그 2배 된 값이 10 이상인 경우
            if num >= 10:
                # 각 자리의 숫자를 더하고 그 수를 3번 공식 내용대로 credit_num_sum에 더해줍니다.
                num = str(num)
                credit_num_sum += int(num[0]) + int(num[1])
            # 2번 공식 내용처럼 그 2배 된 값이 10 미만인 경우
            else:
                # 그 숫자 그대로 3번 공식 내용대로 credit_num_sum에 더해줍니다.
                credit_num_sum += num
        # 1번 공식에서의 맨 우측 수부터 세어 홀수 번째라는 말은
        # 맨 좌측 수부터 세어 짝수 번째라는 말과 같습니다.
        # 따라서 좌측 수부터 세어 짝수 번째라면
        else:
            # 그 숫자 그대로 3번 공식 내용대로 credit_num_sum에 더해줍니다.
            credit_num_sum += int(credit_num[index])

    # 4번 공식 내용대로 credit_num_sum의 값이 10으로 나누어진다면
    if credit_num_sum % 10 == 0:
        # 정당한 번호(유효)이므로 T를 출력합니다.
        print("T")
    # 4번 공식 내용대로 credit_num_sum의 값이 10으로 나누어지지 않는다면
    else:
        # 부당한 번호(유효하지 않음)이므로 F를 출력합니다.
        print("F")