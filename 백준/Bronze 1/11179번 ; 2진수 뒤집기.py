# https://www.acmicpc.net/problem/11179

# 정수 N을 입력하고 정수형으로 변환합니다.
# 1 <= N <= 1,000,000,000
N = int(input())

# 10진수 N을 2진수로 변환하고 앞의 0b를 떼어줍니다.
# 그리고 문자열로 변환한 뒤 역순으로 뒤집어준 변수를 선언합니다.
reversed_bin_N = str(bin(N)[2:])[::-1]
# 2진수의 문자열을 가진 reversed_bin_N을 10진수로 변환해줍니다.
reversed_dec_N = int(reversed_bin_N, 2)

# reversed_dec_N의 값을 출력합니다.
print(reversed_dec_N)
