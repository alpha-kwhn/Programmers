#include <string>
#include <vector>
#include <algorithm>
#include <cmath>
#include <utility>
using namespace std;

string solution(vector<int> numbers, string hand) {
    string answer = "";
    vector<pair<int, int>> pad(12); //키패드 좌표
    vector<pair<int, int>> special(2); //손 짝
    pad[0] = make_pair(0,1); //0의좌표 미리 정의
    int a = 3, b = 0;
    for(int i = 1; i < 10; i++)
    {
        if(b == 3)
        {
            b = 0;
            a--;
        }
        pad[i] = make_pair(a, b);
        b++;
    }
    special[0] = make_pair(0, 2);
    special[1] = make_pair(0, 0);

    for(int i = 0; i < numbers.size(); i++)
    {
        if((numbers[i] % 3 == 0) && numbers[i] != 0)//3, 6, 9
        {
            answer += "R";
            special[0].first = pad[numbers[i]].first;
            special[0].second = pad[numbers[i]].second;
        }
        else if(numbers[i] % 3 == 1)//1, 4, 7
        {
            answer += "L";
            special[1].first = pad[numbers[i]].first;
            special[1].second = pad[numbers[i]].second;
        }
        else if((numbers[i] % 3 == 2) || numbers[i] == 0)//2, 5, 8, 0
        {
            int right_d, left_d;
            right_d = abs(special[0].first - pad[numbers[i]].first) + abs(special[0].second - pad[numbers[i]].second);
            left_d = abs(special[1].first - pad[numbers[i]].first) + abs(special[1].second - pad[numbers[i]].second);
            if(right_d > left_d)
            {
                answer += "L";
                special[1].first = pad[numbers[i]].first;
                special[1].second = pad[numbers[i]].second;
            }
            else if(right_d < left_d)
            {
                answer += "R";
                special[0].first = pad[numbers[i]].first;
                special[0].second = pad[numbers[i]].second;
            }
            else
            {
                if(hand == "right")
                {
                    answer += "R";
                    special[0].first = pad[numbers[i]].first;
                    special[0].second = pad[numbers[i]].second;
                }
                else
                {
                    answer += "L";
                    special[1].first = pad[numbers[i]].first;
                    special[1].second = pad[numbers[i]].second;
                }
            }
        }
    }
    return answer;
}