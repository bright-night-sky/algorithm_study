# https://www.acmicpc.net/problem/10101

# 3개의 줄에 걸쳐 각의 크기를 입력
# 0 <= 각의 크기 <= 180 정수
degree1 = int(input())
degree2 = int(input())
degree3 = int(input())

# 세 각의 합을 저장하는 변수
total_degree = degree1 + degree2 + degree3

# 세 각의 크기가 모두 60이면
if degree1 == 60 and degree2 == 60 and degree3 == 60:
    # Equilateral 출력
    print("Equilateral")
# 세 각의 합이 180이고
elif total_degree == 180:
    # 두 각이 같은 경우
    if degree1 == degree2 or degree2 == degree3 or degree3 == degree1:
        # Isosceles 출력
        print("Isosceles")
    # 같은 각이 없는 경우
    elif degree1 != degree2 and degree2 != degree3 and degree3 != degree1:
        # Scalene 출력
        print("Scalene")
# 세 각의 합이 180이 아닌 경우
elif total_degree != 180:
    # Error 출력
    print("Error")