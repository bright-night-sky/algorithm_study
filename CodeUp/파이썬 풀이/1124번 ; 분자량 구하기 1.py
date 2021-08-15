# https://codeup.kr/problem.php?id=1124

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 화학식을 CxHy꼴로 입력합니다.
# 우리에게 필요한 값은 x, y이므로 입력한 CxHy에서 맨 앞 C는 제외하고,
# xHy에서 H를 기준으로 분리해 x, y값을 만들어줍니다.
# 각각 정수형으로 변환합니다.
x, y = map(int, stdin.readline()[1:].split('H'))
# C의 원자량은 12, H의 원자량은 1이므로, 그에 맞게 CxHy의 분자량을 계산하고 변수에 저장합니다.
molecular_weight = 12 * x + y

# CxHy의 분자량인 molecular_weight의 값을 출력합니다.
print(molecular_weight)