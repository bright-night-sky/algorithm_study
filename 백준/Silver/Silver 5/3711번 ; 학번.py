# https://www.acmicpc.net/problem/3711

# 첫째 줄에 테스트 케이스의 개수 N을 입력합니다.
N = int(input())

for test_case in range(N):
    student_nums = []

    G = int(input())

    for student in range(G):
        student_num = int(input())
        student_nums.append(student_num)

    m = 1
    while True:
        student_num_remainders = []
        is_min_m = True

        for student_num in student_nums:
            remainder = student_num % m
            student_num_remainders.append(remainder)

        for remainder in student_num_remainders:
            if student_num_remainders.count(remainder) >= 2:
                is_min_m = False
                break

        if is_min_m == True:
            print(m)
            break
        else:
            m += 1