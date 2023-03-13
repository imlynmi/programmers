# https://school.programmers.co.kr/learn/courses/30/lessons/118666
# 2022 KAKAO TECH INTERNSHIP - 성격 유형 검사하기

def solution(survey, choices):
    answer = ''
    type_score = {'R':0, 'T':0, 'C':0, 'F':0, 'J':0, 'M':0, 'A':0, 'N':0}
    
    for i, s in enumerate(survey):
        type1 = s[:1]
        type2 = s[1:2]
                
        if choices[i] < 4:
            type_score[type1] += 4 - choices[i]
        elif choices[i] > 4:
            type_score[type2] += choices[i] - 4
    
    answer += "R" if type_score["R"] >= type_score["T"] else "T"
    answer += "C" if type_score["C"] >= type_score["F"] else "F"
    answer += "J" if type_score["J"] >= type_score["M"] else "M"
    answer += "A" if type_score["A"] >= type_score["N"] else "N"
    
    return answer