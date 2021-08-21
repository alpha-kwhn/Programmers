record = ["Enter uid1234 Muzi",
          "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo",
          "Change uid4567 Ryan"]

def solution(record):
    dict = {}
    ans = []
    id = []
    for i in range(len(record)):
        tmp = record[i]
        if tmp[0] == 'E':
            ans.append(tmp[6:])
            dict[i] = "E"
        elif tmp[0] == "C":
            ans.append(tmp[7:])
            dict[i] = "C"
        elif tmp[0] == "L":
            ans.append(tmp[6:])
            dict[i] = "L"      #나갔는지, 들어왔는지, 변경했는지 흐름 순서를 알기 위해서
                               #딕셔너리에 앞글자만 따로 순서대러 저장
                               #슬라이싱으로 아이디와 닉네임만 잘라냄

    id_lis = []
    for i in range(len(ans)): #잘라낸 아이디와 닉네임을 공백기준으로 분리하여 리스트에 재 저장
        id = ans[i].split()
        id_lis.append(id)

    dict2 = {}
    for i in range(len(id_lis)): #딕셔너리의 key에 대응되는 value는 최종으로 갱신된 값만 담는다는 성질 이용
                                #해당 아이디의 닉네임이 최종적으로 무엇으로 변경되었는가를 딕셔너리 형태로 기록한다
        if len(id_lis[i]) > 1:
            dict2[id_lis[i][0]] = id_lis[i][1]
        else:
            continue

    answer = []
    for i in range(len(id_lis)): #Enter, Leave의 흐름을 미리 파악해놓았음
                                #이를 바탕으로 흐름대로 해당 아이디의 최종 닉네임을 딕셔너리를 통해 불러와서
                                #채팅방 문구를 완성시킨다
        if dict[i] == 'E':
            target = dict2[id_lis[i][0]] + "님이 들어왔습니다."
            answer.append(target)
        elif dict[i] == "L":
            target = dict2[id_lis[i][0]] + "님이 나갔습니다."
            answer.append(target)
        else:
            continue
    return answer


did = solution(record)
print(did)