# https://school.programmers.co.kr/learn/courses/30/lessons/92334
# 2022 KAKAO BLIND RECRUITMENT - 신고 결과 받기

def solution(id_list, report, k):
    answer = []
    id_warn = dict(zip(id_list, (0 for _ in id_list)))
    id_report = dict(zip(id_list, ([] for _ in id_list)))
    repeated = dict(zip(report, (0 for _ in report)))
    
    for r in report:
        if repeated[r] == 0:
            repeated[r] = 1
            reporter, reported = r.split(' ')
            id_warn[reported] += 1
            id_report[reporter].append(reported)
        
    for user in id_report.keys():
        email = 0
        for i in id_report[user]:
            if id_warn[i] >= k:
                email += 1
        answer.append(email)
            
    return answer