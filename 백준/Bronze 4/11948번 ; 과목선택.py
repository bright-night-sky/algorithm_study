# https://www.acmicpc.net/problem/11948

# 각 시험의 만점은 100점이다.
# 물리 점수 A 입력
A = int(input())
# 화학 점수 B 입력
B = int(input())
# 생물 점수 C 입력
C = int(input())
# 지구과학 점수 D 입력
D = int(input())
# 역사 점수 E 입력
E = int(input())
# 지리 점수 F 입력
F = int(input())

# 선택한 과목의 총점을 저장하는 변수
total = 0

# 물리, 화학, 생물, 지구과학 점수 중 제일 높은 3과목 점수를 총점에 더해야한다.
# 즉, 제일 낮은 과목만 총점에 더하지 않으면 된다.
science = [A, B, C, D]
min_science = min(science)
total = A + B + C + D - min_science

# 역사, 지리 과목 중에서 더 큰 값을 총점에 더해준다.
total += max(E, F)

# 총점을 출력한다.
print(total)