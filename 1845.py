# https://school.programmers.co.kr/learn/courses/30/lessons/1845
# 해시 - 폰켓몬

def solution(nums):
    choice = len(nums)//2
    types = set(nums)
    
    return choice if len(types) >= choice else len(types)