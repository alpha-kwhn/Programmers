# 점수 동률 -> 사전 순으로 비교
# R/T, C/F, J/M, A/N
def solution(survey, choices):
    dic = {"R": 0, "T": 0, "C": 0, "F": 0, "J": 0, "M": 0, "A": 0, "N": 0}
    mbti = ""
      
    for idx in range(len(survey)):
        if choices[idx] < 4:
            dic[survey[idx][0]] += abs(4-choices[idx])
        elif choices[idx] > 4:
            dic[survey[idx][1]] += abs(4-choices[idx])
    
    mbti += ("T" if dic["R"] < dic["T"] else "R")
    mbti += ("F" if dic["C"] < dic["F"] else "C")
    mbti += ("M" if dic["J"] < dic["M"] else "J")
    mbti += ("N" if dic["A"] < dic["N"] else "A")
    
    return mbti
