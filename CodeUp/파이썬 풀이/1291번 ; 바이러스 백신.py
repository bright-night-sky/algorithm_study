# https://codeup.kr/problem.php?id=1291

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 두 바이러스 번호를 넣었을 때 가장 값싼 백신 번호를 반환하는 함수를 선언합니다.
# 가장 값싼 백신 번호는 두 바이러스 번호의 최대공약수입니다.
def vaccine(num1, num2):
    # 유클리드 호제법을 사용해서 두 숫자의 최대공약수를 구해줍니다.
    # num2의 값이 0이 아니면 계속 반복합니다.
    while num2 != 0:
        # num2의 값은 변수 num1에, num1의 값을 num2의 값으로 나누어 나온 나머지를 변수 num2에 저장합니다.
        num1, num2 = num2, num1 % num2

    # 두 숫자의 최대공약수인 num1의 값을 반환합니다.
    return num1


# 3개의 바이러스 번호를 오름차순으로 공백으로 구분해 입력합니다.
# 1 ~ 3000의 정수입니다.
# 각각 int형으로 변환합니다.
virus1, virus2, virus3 = map(int, stdin.readline().split())
# virus1, virus2의 가장 값싼 백신 번호를 구해 변수 virus1_2_vaccine에 저장합니다.
virus1_2_vaccine = vaccine(virus1, virus2)
# virus1_2_vaccine, virus3의 가장 값싼 백신 번호를 구해 변수 cheapest_vaccine에 저장합니다.
cheapest_vaccine = vaccine(virus1_2_vaccine, virus3)

# 세 바이러스의 가장 값싼 백신 번호를 출력합니다.
print(cheapest_vaccine)
