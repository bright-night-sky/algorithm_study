# https://codeup.kr/problem.php?id=1292

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 도둑으로 의심되는 사람의 DNA를 입력합니다.
# 10자리의 숫자입니다.
# 맨 끝의 \n은 떼어줍니다.
suspect_dna = stdin.readline().rstrip()
# 도둑으로 의심되는 사람의 DNA의 각 자리 숫자의 합을 저장할 변수를 선언합니다.
# 0으로 초기화합니다.
dna_sum = 0

# DNA의 각 자리 숫자를 하나씩 반복해봅니다.
for num in suspect_dna:
    # dna_sum에 현재 자리의 숫자를 더해줍니다.
    dna_sum += int(num)

# dna_sum의 값을 7로 나누었을 때 나머지가 4라면
if dna_sum % 7 == 4:
    # 도둑이므로 문자열 'suspect'를 출력합니다.
    print('suspect')
# 그렇지 않다면
else:
    # 도둑이 아니므로 문자열 'citizen'을 출력합니다.
    print('citizen')