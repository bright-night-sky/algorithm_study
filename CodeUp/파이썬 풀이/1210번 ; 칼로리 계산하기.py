# https://codeup.kr/problem.php?id=1210

# readline을 사용하기 위해 import합니다.
from sys import stdin


# 문제에서 주어진 메뉴의 번호 순서에 따라 칼로리 값들로 구성된 리스트를 만들어줍니다.
menus_calorie = [400, 340, 170, 100, 70]
# 메뉴의 번호 두 개를 공백으로 구분해 입력합니다.
num1, num2 = map(int, stdin.readline().split())
# 입력한 각 메뉴의 번호에 해당하는 음식의 칼로리들을 더하고, 그 값을 변수에 저장합니다.
calorie_sum = menus_calorie[num1 - 1] + menus_calorie[num2 - 1]

# 칼로리의 합이 500보다 크면
if calorie_sum > 500:
    # 문자열 'angry'를 출력합니다.
    print('angry')
# 그 외의 경우, 즉 500 이하라면
else:
    # 문자열 'no angry'를 출력합니다.
    print('no angry')