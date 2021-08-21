#include <string>
#include <vector>
#include <map>
using namespace std;

int solution(vector<vector<string>> clothes) {
	int answer = 0;
	int count = 0;
	map<string, int> m1;
	map<string, int>::iterator itr;
	for (int i = 0; i < clothes.size(); i++)
		m1[clothes[i][1]]++;
    answer = 1;
	for (itr = m1.begin(); itr != m1.end(); itr++)
		answer *= (itr->second + 1);
	--answer; //다 안입는경우
	return answer;
}