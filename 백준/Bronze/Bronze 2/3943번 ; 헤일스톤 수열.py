# https://www.acmicpc.net/problem/3943

# 첫째 줄에 테스트 케이스의 개수 T를 입력합니다.
# 1 <= T <= 100,000
T = int(input())

for test_case_index in range(T):
    n = int(input())

    sequence = [n]

    while True:
        last_number = sequence[-1]

        if last_number == 1:
            break
        else:
            if last_number % 2 == 0:
                next_number = int(last_number / 2)
                sequence.append(next_number)
            else:
                next_number = last_number * 3 + 1
                sequence.append(next_number)

    max_num = max(sequence)

    print(max_num)