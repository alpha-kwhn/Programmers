#include <iostream>
#include <stdio.h>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int solution(vector<int> d, int budget) {
    int answer = 0;
    int sum = 0;
    int sum2 = 0;
    int count = 0;
    for(int i = 0; i < d.size(); i++)
        sum += d[i];
    if(sum == budget)
        answer = d.size();
    else
    {
        sort(d.begin(), d.end());
        for(int i = 0; i < d.size(); i++)
        {
            sum2 += d[i];
            if(sum2 <= budget)
                count++;
            else
                break;
        }
        answer = count;
    }
    return answer;
}