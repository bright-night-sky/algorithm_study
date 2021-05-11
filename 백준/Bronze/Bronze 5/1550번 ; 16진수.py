# https://www.acmicpc.net/problem/1550

# 16진수 수 입력
# 최대 길이 : 6글자
# 0 ~ 9와 A ~ F로 이루어져 있다.
# 음이 아닌 정수로 입력
hex_num = '0x' + input()

# 입력받은 16진수 수를 10진수로 변환해서 저장하는 변수
ten_num = int(hex_num, 16)

# 출력
print(ten_num)