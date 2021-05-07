# https://www.acmicpc.net/problem/1373

# 첫째 줄에 2진수를 입력합니다.
# 입력한 2진수를 10진수로 변환해줍니다.
bin_to_dec_num = int(input(), 2)

# 변환된 10진수를 8진수로 변환해서 저장한 변수를 선언합니다.
oct_num = oct(bin_to_dec_num)

# 8진수로 변환된 결과에서 맨 앞의 0o를 떼주고 출력합니다.
print(oct_num[2:])