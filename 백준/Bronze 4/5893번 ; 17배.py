# https://www.acmicpc.net/problem/5893

# 이진수 N 입력
# 최대 1000자리 이진수
# 0 입력은 없음
# 입력받은 이진수 문자열 앞에 0b를 붙이고 int 함수를 이용해 10진수로 변환
N = int('0b' + input(), 2)

# 17을 곱하고 이진수로 변환
bin_result_17_multi = bin(N * 17)

# 이진수를 출력할 때는 앞에 0b가 붙어서 나오므로 출력형식에 맞게 0b를 제거해서 출력
print(bin_result_17_multi[2:])
