s = "one4seveneight"

def solution(s):
    num_list = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    dic = {"zero":0, "one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9}
    result = ""
    answer = []
    for i in range(len(s)):
        result += s[i]
        if result in num_list:
            answer.append(dic[result])
            result = ""
        elif result.isdigit():
            answer.append(int(result))
            result = ""
    result = list(map(str, answer))
    str1 = ''.join(result)
    ans = int(str1)

    return ans

did = solution(s)
print(did)