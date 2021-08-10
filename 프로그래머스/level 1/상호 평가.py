# https://programmers.co.kr/learn/courses/30/lessons/83201

# 학생들의 점수가 담긴 정수형 2차원 리스트 scores가 매개변수로 주어집니다.
def solution(scores):
    # 학생들의 학점을 순서대로 문자열로 저장할 변수를 선언합니다.
    grades = ''
    # 학생들의 수를 저장하는 변수를 선언합니다.
    student_cnt = len(scores)

    # 0번 학생부터 끝까지 한 명씩 반복해봅니다.
    for student_num in range(student_cnt):
        # 현재 번호의 학생이 받은 점수들을 저장할 리스트 변수를 선언합니다.
        cur_student_scores = []

        # 자기 자신을 포함한 모든 학생들이 현재 번호의 학생에 준 점수를 반복문으로 확인해봅니다.
        for idx in range(student_cnt):
            # 과제를 평가한 점수를 저장하는 변수를 선언합니다.
            score = scores[idx][student_num]
            # cur_student_scores에 점수를 넣어줍니다.
            cur_student_scores.append(score)

        # 현재 번호의 학생이 받은 점수 중 가장 높은 점수를 저장하는 변수를 선언합니다.
        max_score = max(cur_student_scores)
        # 점수 중에서 가장 높은 점수의 개수를 저장하는 변수를 선언합니다.
        max_cnt = cur_student_scores.count(max_score)
        # 현재 번호의 학생이 받은 점수 중 가장 낮은 점수를 저장하는 변수를 선언합니다.
        min_score = min(cur_student_scores)
        # 점수 중에서 가장 낮은 점수의 개수를 저장하는 변수를 선언합니다.
        min_cnt = cur_student_scores.count(min_score)
        # 현재 번호의 학생이 자기 자신한테 평가한 점수를 저장하는 변수를 선언합니다.
        self_score = cur_student_scores[student_num]
        # 현재 번호의 학생이 받은 점수들의 합을 저장하는 변수를 선언합니다.
        score_sum = sum(cur_student_scores)
        # 현재 번호의 학생이 받은 점수 개수를 저장하는 변수를 선언합니다.
        score_cnt = len(cur_student_scores)

        # 현재 번호의 학생이 자기 자신한테 평가한 점수가 가장 높은 점수이며, 그 점수가 유일한 최고점이라면
        if max_score == self_score and max_cnt == 1:
            # 점수 합계에서 자기 자신한테 평가한 점수를 빼줍니다.
            score_sum -= self_score
            # 점수의 개수에도 한 개를 빼줍니다.
            score_cnt -= 1
        # 현재 번호의 학생이 자기 자신한테 평가한 점수가 가장 낮은 점수이며, 그 점수가 유일한 최저점이라면
        elif min_score == self_score and min_cnt == 1:
            # 점수 합계에서 자기 자신한테 평가한 점수를 빼줍니다.
            score_sum -= self_score
            # 점수의 개수에도 한 개를 빼줍니다.
            score_cnt -= 1

        # 현재 번호의 학생의 평균을 저장하는 변수를 선언합니다.
        avg = score_sum / score_cnt

        # 평균이 90점 이상이라면
        if avg >= 90:
            # grade에 A를 넣어줍니다.
            grades += 'A'
        # 평균이 80점 이상 90점 미만이라면
        elif 80 <= avg < 90:
            # grade에 B를 넣어줍니다.
            grades += 'B'
        # 평균이 70점 이상 80점 미만이라면
        elif 70 <= avg < 80:
            # grade에 C를 넣어줍니다.
            grades += 'C'
        # 평균이 50점 이상 70점 미만이라면
        elif 50 <= avg < 70:
            # grade에 D를 넣어줍니다.
            grades += 'D'
        # 그 외의 경우, 즉, 평균이 50점 미만이라면
        else:
            # grade에 F를 넣어줍니다.
            grades += 'F'

    # 학생들의 학점들을 반환합니다.
    return grades