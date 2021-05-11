# https://www.acmicpc.net/problem/9506

# -1을 입력할 때까지 반복합니다.
while True:
    # n을 입력합니다.
    # 2 < n < 100,000
    n = int(input())

    # 입력한 n이 -1이라면
    if n == -1:
        # 반복문을 탈출하고 종료합니다.
        break
    # 입력한 n이 다른 숫자라면
    else:
        # 진약수들을 저장하는 리스트 변수를 선언합니다.
        proper_divisor = []
        # 진약수들의 합을 저장하는 변수를 선언합니다.
        proper_divisor_sum = 0

        # 1부터 n의 절반까지 반복해봅니다.
        for num in range(1, n // 2 + 1):
            # n이 현재 숫자로 나누어 떨어진다면
            if n % num == 0:
                # 현재 숫자는 n의 약수이므로 문자열로 변환해 진약수 리스트 변수에 넣어줍니다.
                proper_divisor.append(str(num))
                # 현재 숫자를 진약수들의 합에 더해줍니다.
                proper_divisor_sum += num

        # 진약수의 합이 n과 같다면
        if proper_divisor_sum == n:
            # 출력 형식에 맞게 출력합니다.
            print(f"{n} = " + ' + '.join(proper_divisor))
        # 진약수의 합이 n과 다르다면
        else:
            # 출력 형식에 맞게 출력합니다.
            print(f"{n} is NOT perfect.")