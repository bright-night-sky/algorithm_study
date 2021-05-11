# https://www.acmicpc.net/problem/2747

# 첫째 줄에 n을 입력합니다.
# n은 45보다 작거나 같은 자연수입니다.
n = int(input())

# 피보나치 수를 출력하는 함수입니다.
def fibonacci(n):
    # 피보나치 수들을 차례대로 저장하는 변수입니다.
    fibo_list = [0, 1]

    # 0번째 피보나치 수는
    if n == 0:
        # 0이므로 0을 반환합니다.
        return fibo_list[0]
    # 1번째 피보나치 수는
    elif n == 1:
        # 1이므로 1을 반환합니다.
        return fibo_list[1]
    # 2번째 이상의 피보나치 수는
    else:
        # 2번째 이상의 피보나치 수를 구하면서 fibo_list에 넣어줍니다.
        for i in range(2, n+1):
            fibo_list.append(fibo_list[i-1]+fibo_list[i-2])
        # n번째 피보나치 수를 반환합니다.
        return fibo_list[n]

# n번째 피보나치 수를 출력합니다.
print(fibonacci(n))