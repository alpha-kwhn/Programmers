import re
files = ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]


def solution(files):
    answer = []

    for i in range(len(files)):
        total = re.split("([0-9]+)", files[i])
        answer.append(total)
    answer = sorted(answer, key = lambda x : (x[0].lower(), int(x[1])))
    return [''.join(tmp) for tmp in answer]

        #[0-9] 숫자 범위를 나타내는 메타 캐릭터
        #()의 의미 : 그루핑 --> 매칭 결과를 각 그룹별로 분리해서 볼 수 있다
        # +를 쓰면 --> 문자 하나하나씩이 아닌 단어 별로 분리가능


did = solution(files)
print(did)