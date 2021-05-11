# https://www.acmicpc.net/problem/5073

# 0 0 0을 입력할 때까지 계속 입력받는다.
while True:
    # 1,000을 넘지 않는 양의 정수 3개 입력
    num1, num2, num3 = map(int, input().split(' '))

    # 가장 긴 변을 저장하는 변수
    longest = max(num1, num2, num3)
    # 나머지 두 변의 합
    remains = num1 + num2 + num3 - longest

    # 0 0 0을 입력한 경우
    if num1 == 0 and num2 == 0 and num3 == 0:
        # 반복문 탈출
        break
    # 다른 숫자들을 입력한 경우
    else:
        # 가장 긴 변의 길이보다 나머지 두 변의 길이의 합이 길지 않으면
        if longest >= remains:
            # Invalid 출력
            print("Invalid")
        # 세 변의 길이가 모두 같은 경우
        elif num1 == num2 == num3:
            # Equilateral 출력
            print("Equilateral")
        # 두 변의 길이만 같은 경우
        elif num1 == num2 or num2 == num3 or num1 == num3:
            # Isosceles 출력
            print("Isosceles")
        # 세 변의 길이가 모두 다른 경우
        elif num1 != num2 != num3:
            # Scalene 출력
            print("Scalene")