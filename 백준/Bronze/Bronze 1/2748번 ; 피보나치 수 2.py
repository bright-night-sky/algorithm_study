# https://www.acmicpc.net/problem/2748

# 첫째 줄에 n 입력
# 90보다 작거나 같은 자연수
n = int(input())

# n번째 피보나치 수를 구하는 함수 생성
def fibonacci(n):
    # 피보나치 수들을 저장하는 리스트 변수
    fibo_num = [0, 1]

    # 0번째 피보나치 수는
    if n == 0:
        # 0이므로 0을 반환
        return fibo_num[0]
    # 1번째 피보나치 수는
    elif n == 1:
        # 1이므로 1을 반환
        return fibo_num[1]
    # 2번째 이상 피보나치 수는
    else:
        # 피보나치 수를 구하는 공식을 사용하여
        # n번째 피보나치 수를 구할 때까지 fibo_num 리스트 변수에 피보나치 수를 쌓아나간다.
        for i in range(2, n+1):
            fibo_num.append(fibo_num[i-1] + fibo_num[i-2])
        # n번째 피보나치 수까지 저장되어 있는 리스트 fibo_num에서 n번째 피보나치 수를 반환
        return fibo_num[n]

# n번째 피보나치 수를 출력
print(fibonacci(n))