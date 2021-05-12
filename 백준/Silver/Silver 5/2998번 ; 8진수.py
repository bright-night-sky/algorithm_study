# https://www.acmicpc.net/problem/2998

# readline을 사용하기 위해 import합니다.
from sys import stdin

# 2진수 3자리를 8진수로 바꾸는 방법을 저장하고 있는 dictionary 변수를 선언합니다.
bin_to_oct_dict = {
    '000': 0,
    '001': 1,
    '010': 2,
    '011': 3,
    '100': 4,
    '101': 5,
    '110': 6,
    '111': 7
}

# 첫째 줄에 2진수를 입력합니다.
# 100자리 이내이고, 첫 번째 자리는 1입니다.
bin_num = stdin.readline().rstrip()
# 입력한 2진수의 길이를 저장하는 변수입니다.
bin_num_len = len(bin_num)

# 2진수의 길이를 3으로 나누었을 때 나머지가 1이라면
if bin_num_len % 3 == 1:
    # 앞에 00을 붙여줍니다.
    bin_num = '00' + bin_num
# 2진수의 길이를 3으로 나누었을 때 나머지가 2라면
elif bin_num_len % 3 == 2:
    # 앞에 0을 붙여줍니다.
    bin_num = '0' + bin_num

# 2진수의 길이를 다시 초기화해줍니다.
bin_num_len = len(bin_num)

# 2진수를 8진수로 바꾼 뒤의 결과를 저장할 변수를 선언합니다.
oct_num = ''

# 2진수를 3자리씩 끊어서 반복해봅니다.
for idx in range(0, bin_num_len, 3):
    # 2진수의 세 자리를 8진수로 바꿔 저장하는 변수를 선언합니다.
    one_oct_num = bin_to_oct_dict[bin_num[idx:idx+3]]
    # one_oct_num을 문자열로 변환해 oct_num에 넣어줍니다.
    oct_num += str(one_oct_num)

# 2진수를 8진수로 바꾼 결과를 출력합니다.
print(oct_num)