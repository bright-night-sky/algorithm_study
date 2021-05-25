# https://www.acmicpc.net/problem/1439

# readline을 사용하기 위해 import합니다.
from sys import stdin

# 첫째 줄에 1과 0으로만 이루어진 문자열 S를 입력합니다.
# S의 길이는 100만보다 작습니다.
S = stdin.readline().rstrip()

# 문자열 S에서 연속된 1로만 이루어진 구간들을 저장하는 리스트 변수를 선언합니다.
one_sections = list(filter(lambda section: section != '', S.split('0')))
# 문자열 S에서 연속된 0으로만 이루어진 구간들을 저장하는 리스트 변수를 선언합니다.
zero_sections = list(filter(lambda section: section != '', S.split('1')))

# 연속된 1로만 이루어진 구간들의 개수를 저장하는 변수를 선언합니다.
one_sections_cnt = len(one_sections)
# 연속된 0으로만 이루어진 구간들의 개수를 저장하는 변수를 선언합니다.
zero_sections_cnt = len(zero_sections)

# 연속된 1로만 이루어진 구간들의 개수와 연속된 0으로만 이루어진 구간들의 개수 중 더 작은 것의 개수를 출력합니다.
print(min(one_sections_cnt, zero_sections_cnt))