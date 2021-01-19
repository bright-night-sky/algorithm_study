# acmicpc.net/problem/5086

while True:
    # 두 수를 입력하는 테스트 케이스 입력
    num1, num2 = map(int, input().split(' '))

    # 만약 입력된 두 수가 0, 0이라면
    if num1 == 0 and num2 == 0:
        # 종료
        break

    # 첫 번째 숫자가 두 번째 숫자의 약수이면
    if num2 % num1 == 0:
        # factor 출력
        print("factor")
    # 첫 번째 숫자가 두 번째 숫자의 배수이면
    elif num1 % num2 == 0:
        # multiple 출력
        print("multiple")
    # 첫 번째 숫자가 두 번째 숫자의 약수와 배수 모두 아니면
    else:
        # neither 출력
        print("neither")