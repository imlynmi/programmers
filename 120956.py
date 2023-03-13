# https://school.programmers.co.kr/learn/courses/30/lessons/120956
# 코딩테스트 입문 - 옹알이 (1)


def solution(babbling):
    answer = 0
    base = ["aya", "ye", "woo", "ma"]
    
    for b in babbling:
        sound = ''
        for l in b:
            sound += l
            if sound in base:
                sound = ''
        if sound == '':
            answer += 1
    
    return answer