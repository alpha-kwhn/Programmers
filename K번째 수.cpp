#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> array, vector<vector<int>> commands) {
    vector<int> answer;
    vector<int> deposit; //추출된 배열 일부를 저장하는 곳
    for(int i = 0; i < commands.size(); i++) //2차원 배열 commands의 사이즈 만큼 for문 반복해서 answer에 값을 넣어줌
    {
        deposit.assign(array.begin() + commands[i][0] - 1, array.begin() + commands[i][1]);//추출 구간 시작점 -1 부터 추출 구간 끝점 직전까지 deposit에 복사
        sort(deposit.begin(), deposit.end()); //추출한 배열 오름차순으로 정리
        answer.push_back(deposit[commands[i][2] -1]); //commands[i][2] 번째 index, 즉 탐색위치에 있는 갑을 answer 배열에 투입
    }
    return answer;
}