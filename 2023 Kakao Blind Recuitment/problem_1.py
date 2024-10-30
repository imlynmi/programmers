# 날짜 배열을 자르고 총 일수로 계산
def date_to_days(date):
    y, m, d = map(int, date.split("."))
    days = y * 12 * 28 + m * 28 + d

    return days

def solution(today, terms, privacies):
    result = []

    # 오늘의 날짜로 총 일수를 계산하는 함수 호출
    tdy_days = date_to_days(today)

    # 'terms'를 dictionary로 전환 -> {약관 종류(t[0:1]): 약관 기간 일수(int(t[2:]) * 28)}
    terms_dict = {}
    for t in terms:
        terms_dict[t[0:1]] = int(t[2:]) * 28

    signed_seq = 0  # 약관 서수 추적
    for p in privacies:
        signed_seq += 1     #몇번째 약관
        signed_days = date_to_days(p[0:10])     #약관 채결 날짜로 총 일수를 계산하는 함수 호출
        signed_type = p[11:12]      # 약관 종류 추출
        term_len = terms_dict[signed_type]      # 'terms' dictionary에서 약관 기한 추출
        exp_days = signed_days + term_len       # 약관 기한 계산
        
        # 약관 기한과 오늘 비교, 짧거나 같으면 파기해야 하니 result 베열에 약관 서수를 기입
        if exp_days <= tdy_days:
            result.append(signed_seq)

    return result

solution("2020.01.01", ["Z 3", "D 5"], ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"])