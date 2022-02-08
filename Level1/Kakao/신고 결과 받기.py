report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
id_list = ["muzi", "frodo", "apeach", "neo"]
report2 = ["ryan con", "ryan con", "ryan con", "ryan con"]
id_list2 = ["con", "ryan"]
k1 = 2
k2 = 3

#한 유저에 대한 신고는 계속 할 수 있으나, 횟수는 1회로 고정됨
#k번 이상 신고된 유저는 게시판 이용이 정지당함, 그리고 그 유저를 신고한 모든 사람들에게 메일 전송
#


def solution(id_list, report, k):

    #처벌받은 횟수 집계 Dictionary 생성
    dic = {}
    dics = {}
    for i in id_list:
        dic[i] = 0
        dics[i] = 0

    # 신고자와 처벌자를 구분해서 새로운 리스트 생성후 --> 2차원으로 넣어줌
    new_report = []
    newer_report = []
    for i in report:
        new_report.append(i.split())

    for v in new_report:
        if v not in newer_report:
            newer_report.append(v)

    # 처벌받은 수 세기
    penalty = []
    for i in newer_report:
        dic[i[1]] += 1
    for i in range(0, len(id_list)):
        penalty.append(dic[id_list[i]])

    for i in range(len(penalty)):
        if penalty[i] >= k:
            for j in newer_report:
                if j[1] == id_list[i]:
                    dics[j[0]] += 1

    answer = []
    for i in range(len(dics)):
        answer.append(dics[id_list[i]])

    return answer










print(solution(id_list2, report2, k2))




