#include <string>
#include <vector>
#include <iostream>
using namespace std;

vector<int> solution(vector<int> prices) {
	vector<int> answer;
	int count = 0;
	for (int i = 0; i < prices.size() - 1; i++)
	{
		for (int k = i + 1; k < prices.size(); k++)
		{
			count++;
			if (prices[i] > prices[k])
				break;
		}
		answer.push_back(count);
		count = 0;
	}
	answer.push_back(0);
	return answer;
}