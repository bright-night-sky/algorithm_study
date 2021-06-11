# https://www.acmicpc.net/problem/14626

# readline을 사용하기 위해 import합니다.
from sys import stdin

# ISBN 13자리 숫자를 입력합니다.
# 훼손된 숫자 하나를 *로 입력합니다.
isbn = stdin.readline().rstrip()
# ISBN의 길이를 저장하는 변수를 선언합니다.
isbn_len = len(isbn)
# ISBN에서 *을 제외한 숫자들의 a+3b+c+3d+e+3f+g+3h+i+3j+k+3l+m의 결과를 저장하는 변수를 선언합니다.
except_star = 0
# *의 인덱스를 저장하는 변수를 선언합니다.
star_idx = None

# ISBN의 각 숫자를 하나씩 반복해봅니다.
for idx in range(isbn_len):
    # 현재 자리의 숫자가 *이라면
    if isbn[idx] == '*':
        # star_idx에 현재 인덱스 값을 저장합니다.
        star_idx = idx
        # 다음으로 넘어갑니다.
        continue
    # 현재 자리 인덱스 값을 2로 나누었을 때 나머지가 0이라면
    elif idx % 2 == 0:
        # except_star에 현재 자리에 맞는 숫자값을 더해줍니다.
        except_star += int(isbn[idx])
    # 현재 자리 인덱스 값을 2로 나누었을 때 나머지가 1이라면
    elif idx % 2 == 1:
        # except_star에 현재 자리에 맞는 숫자값을 더해줍니다.
        except_star += int(isbn[idx]) * 3

# 0부터 9까지 반복합니다.
for number in range(10):
    # star_idx를 2로 나누었을 때 나머지가 0이라면
    if star_idx % 2 == 0:
        # except_star와 number의 합을 10으로 나누었을 때 나머지가 0이라면
        if (except_star + number) % 10 == 0:
            # number를 출력하고 반복문을 탈출합니다.
            print(number)
            break
    # star_idx를 2로 나누었을 때 나머지가 1이라면
    else:
        # except_star와 number * 3의 합을 10으로 나누었을 때 나머지가 0이라면
        if (except_star + number * 3) % 10 == 0:
            # number를 출력하고 반복문을 탈출합니다.
            print(number)
            break