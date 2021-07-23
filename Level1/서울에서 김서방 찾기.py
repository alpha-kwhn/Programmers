seoul = ["Jane", "Kim"]

def solution(seoul):
    str1 = "김서방은 "
    str2 = "에 있다"
    str3 = str(seoul.index("Kim"))
    answer = str1 + str3 + str2
    return answer
did = solution(seoul)
print(did)
