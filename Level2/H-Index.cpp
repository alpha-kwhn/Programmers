#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<int> citations) {
	int answer = 0;
	vector<int> con;
	int find_max = *max_element(citations.begin(), citations.end());
	if (find_max == 0)
		return 0;
	else
	{
		for (int i = 1; i <= citations.size(); i++)
		{
			int count = 0;
			for (int j = 0; j < citations.size(); j++)
			{
				if (citations[j] >= i)
					count++;
			}
			if ((count >= i) && (i >= citations.size() - count))
				con.push_back(i);
		}

		int max = *max_element(con.begin(), con.end());
		answer = max;
		return answer;
	}
}