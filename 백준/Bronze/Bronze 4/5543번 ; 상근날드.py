# https://www.acmicpc.net/problem/5543

# 상덕버거 가격 입력
sangduk = int(input())
# 중덕버거 가격 입력
joongduk = int(input())
# 하덕버거 가격 입력
haduk = int(input())
# 콜라 가격 입력
cola = int(input())
# 사이다 가격 입력
cider = int(input())

# 가장 싼 세트 메뉴의 가격은 제일 싼 버거와 제일 싼 음료의 가격 합에서 50원을 뺀 것이다.
# 가장 싼 버거의 가격을 저장하는 변수
min_burger = min(sangduk, joongduk, haduk)
# 가장 싼 음료의 가격을 저장하는 변수
min_drink = min(cola, cider)
# 가장 싼 세트의 가격을 저장하는 변수
min_set = min_burger + min_drink - 50

# 가장 싼 세트의 가격을 출력
print(min_set)