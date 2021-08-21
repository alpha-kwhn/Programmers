#include <string>
#include <vector>
#include <map>
#include <queue>
#include <algorithm>
using namespace std;

int solution(vector<int> priorities, int location) {
	int answer = 0;
	int value = 0;
	int locate = 0;
	queue<int> tmp;
	vector<pair<int, int>> test;
	queue<pair<int, int>> ptr;

	for (int i = 0; i < priorities.size(); i++)
		test.push_back(make_pair(priorities[i], i));

	//for (int p = 0; p < priorities.size(); p++)
	//ptr.push(make_pair(priorities[p], p));
	//if(value == *max_element(test.begin(), test.end()));

	while (1)
	{

		value = test[0].first;
		locate = test[0].second;
		int count = 0;

		for (int i = 1; i < test.size(); i++)
		{
			if (value < test[i].first)
			{
				count = 1;
			}
		}

		if ((count == 0) && (locate == location))
		{
			answer++;
			break;
		}
		else if ((count == 0) && (locate != location))
		{
			answer++;
			test.erase(test.begin());
		}
		else if (count == 1)
		{
			test.push_back(make_pair(value, locate));
			test.erase(test.begin());
		}
	}
	return answer;
}

void main()
{
	vector<int>priorities;
	priorities.push_back(2);
	priorities.push_back(1);
	priorities.push_back(3);
	priorities.push_back(2);
	int loc = 2;
	int ttt = solution(priorities, loc);
	cout << ttt << endl;

	vector<int>pro;
	priorities.push_back(1);
	priorities.push_back(1);
	priorities.push_back(9);
	priorities.push_back(1);
	priorities.push_back(1);
	priorities.push_back(1);
	loc = 0;
	ttt = solution(pro, loc);
	cout << ttt << endl;
}