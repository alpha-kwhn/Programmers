phone_book = ["119", "97674223", "1195524421"]


def solution(phone_book):
    answer = True
    phone_book.sort()

    for i in range(1, len(phone_book)):
        if phone_book[i-1][0:len(phone_book[i-1])] == phone_book[i][0:len(phone_book[i-1])]:
            return False
        # 효율성 3, 4번 해결
        # 사전순으로 str 정렬을 하였을 때, 바로 옆 전화번호가 현재 인덱스의 전화번호를 접두어로 안가지면
        # 그 뒤에는 절대 없다는 성질을 이용하였음
        else:
            continue
    return answer

did = solution(phone_book)
print(did)