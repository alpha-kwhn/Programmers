#include <string>
#include <stack>
#include <cctype>
using namespace std;

int solution(string dartResult) {
    int len = dartResult.length();
    int answer = 0;
    int tmp = 0;
    int arr[3];
    stack<int> s;
    for(int i = 0; i < len; i++)
    {
        if ((dartResult[i] == 'D') && (dartResult[i + 1] == '#'))
        {
            if ((dartResult[i - 1] == '0') && (dartResult[i - 2] == '1')) //10일 때
                s.push(-100);
            else
                s.push((dartResult[i - 1] - '0') * (dartResult[i - 1] - '0') * -1); //그 외
        }
        else if ((dartResult[i] == 'T') && (dartResult[i + 1] == '#'))
        {
            if ((dartResult[i - 1] == '0') && (dartResult[i - 2] == '1')) //10일 때
                s.push(-1000);
            else
                s.push((dartResult[i - 1] - '0') * (dartResult[i - 1] - '0') * (dartResult[i - 1] - '0') * -1); //그 외
        }
        else if ((dartResult[i] == 'S') && (dartResult[i + 1] == '#'))
        {
            if ((dartResult[i - 1] == '0') && (dartResult[i - 2] == '1')) //10일 때
                s.push(-10);
            else
                s.push((dartResult[i - 1] - '0') * -1); //그 외
        }
        else if ((dartResult[i] == 'D') && (dartResult[i + 1] == '*'))
        {
            if ((dartResult[i - 1] == '0') && (dartResult[i - 2] == '1')) //10일 때
            {
                tmp = s.top();
                s.pop();
                s.push(2 * tmp);
                s.push(200);
            }
            else
            {
                tmp = s.top();
                s.pop();
                s.push(2 * tmp);
                s.push((dartResult[i - 1] - '0') * (dartResult[i - 1] - '0') * 2);
            }
        }
        else if ((dartResult[i] == 'T') && (dartResult[i + 1] == '*'))
        {
            if ((dartResult[i - 1] == '0') && (dartResult[i - 2] == '1')) //10일 때
            {
                tmp = s.top();
                s.pop();
                s.push(2 * tmp);
                s.push(2000);
            }
            else
            {
                tmp = s.top();
                s.pop();
                s.push(2 * tmp);
                s.push((dartResult[i - 1] - '0') * (dartResult[i - 1] - '0') * (dartResult[i - 1] - '0') * 2);
            }
        }
        else if ((dartResult[i] == 'S') && (dartResult[i + 1] == '*'))
        {
            if ((dartResult[i - 1] == '0') && (dartResult[i - 2] == '1')) //10일 때
            {
                tmp = s.top();
                s.pop();
                s.push(2 * tmp);
                s.push(20);
            }
            else
            {
                tmp = s.top();
                s.pop();
                s.push(2 * tmp);
                s.push((dartResult[i - 1] - '0') * 2);
            }
        }
        else if ((dartResult[i] == 'D') && (isdigit(dartResult[i + 1]) == 1))
        {
            if ((dartResult[i - 1] == '0') && (dartResult[i - 2] == '1')) //10일 때
                s.push(100);
            else
                s.push((dartResult[i - 1] - '0') * (dartResult[i - 1] - '0')); //그 외
        }
        else if ((dartResult[i] == 'T') && (isdigit(dartResult[i + 1]) == 1))
        {
            if ((dartResult[i - 1] == '0') && (dartResult[i - 2] == '1')) //10일 때
                s.push(1000);
            else
                s.push((dartResult[i - 1] - '0') * (dartResult[i - 1] - '0') * (dartResult[i - 1] - '0')); //그 외
        }
        else if ((dartResult[i] == 'S') && (isdigit(dartResult[i+1]) == 1))
        {
            if ((dartResult[i - 1] == '0') && (dartResult[i - 2] == '1')) //10일 때
                s.push(10);
            else
                s.push((dartResult[i - 1] - '0')); //그 외
        }
        else if ((dartResult[i] == 'D') && (i == len - 1))
        {
            if ((dartResult[i - 1] == '0') && (dartResult[i - 2] == '1')) //10일 때
                s.push(100);
            else
                s.push((dartResult[i - 1] - '0') * (dartResult[i - 1] - '0')); //그 외
        }
        else if ((dartResult[i] == 'T') && (i == len - 1))
        {
            if ((dartResult[i - 1] == '0') && (dartResult[i - 2] == '1')) //10일 때
                s.push(1000);
            else
                s.push((dartResult[i - 1] - '0') * (dartResult[i - 1] - '0') * (dartResult[i - 1] - '0')); //그 외
        }
        else if ((dartResult[i] == 'S') && (i == len - 1))
        {
            if ((dartResult[i - 1] == '0') && (dartResult[i - 2] == '1')) //10일 때
                s.push(10);
            else
                s.push((dartResult[i - 1] - '0')); //그 외
        }
    }
    for (int k = 0; k < 3; k++)
        arr[k] = NULL;//배열 초기화
    for (int k = 0; k < 3; k++)
    {
        arr[k] = s.top();
        s.pop(); //stack
    }
    for (int k = 0; k < 3; k++)
        answer += arr[k];
    return answer;
}
