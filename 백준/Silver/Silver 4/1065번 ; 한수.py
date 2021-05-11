# https://www.acmicpc.net/problem/1065

# 첫째 줄에 1,000보다 작거나 같은 자연수 N을 입력합니다.
N = int(input())

# N이 100 미만이라면
if N < 100:
    # 100 미만의 숫자들은 모두 한수에 속하므로 N을 그대로 출력해줍니다.
    print(N)
# N이 100 이상이라면
else:
    # 한수의 개수를 저장할 변수를 선언합니다.
    # 100 미만의 숫자들은 모두 한수에 속하므로 99로 초기화해줍니다.
    han_num_count = 99

    # 100부터 N까지 반복해봅니다.
    for number in range(100, N + 1):
        # 현재 숫자를 문자열 형태로 변환하고 저장하는 변수를 선언합니다.
        str_num = str(number)
        # 현재 숫자의 길이를 저장하는 변수를 선언합니다.
        num_len = len(str_num)
        # 현재 숫자의 맨 앞자리와 맨 뒷자리 숫자의 차이를 공차로 저장하는 변수를 선언합니다.
        common_difference = int(str_num[1]) - int(str_num[0])
        # 현재 숫자가 한수인지 여부를 저장하는 변수를 선언합니다.
        # 한수가 맞다는 뜻인 True로 초기화합니다.
        is_han = True

        # 현재 숫자의 두 번째 숫자부터 뒤에서 두 번째 숫자까지 반복해봅니다.
        for index in range(1, num_len - 1):
            # 현재 자리의 숫자 - 다음 자리의 숫자가 공차와 같지 않다면
            if int(str_num[index + 1]) - int(str_num[index]) != common_difference:
                # 현재 숫자는 한수가 아니므로 is_han의 값을 False로 변경합니다.
                is_han = False
                # 반복문을 탈출합니다.
                break

        # 현재 숫자가 한수라면
        if is_han:
            # 한수의 개수에 1을 더해줍니다.
            han_num_count += 1

    # 한수의 개수를 출력합니다.
    print(han_num_count)