#include <string>
#include <vector>
#include <stack>
#include <algorithm>
#include <queue>
using namespace std;

int solution(string skill, vector<string> skill_trees)
{
	int answer = 0;
	int check = 0;
	queue<int> test;
	queue<int> test2;
	for (int t = 0; t < skill.length(); t++)
		test2.push(skill[t]);

	for (int j = 0; j < skill_trees.size(); j++)
	{
		for (int i = 0; i < skill_trees[j].length(); i++)
		{
			for (int p = 0; p < skill.length(); p++)
			{
				if (skill_trees[j][i] == skill[p])
					test.push(skill[p]);
			}
		}
		if (test.size() == 0)
			answer++;
		else if (test.front() != test2.front())
		{
			while (!test.empty())
				test.pop();
		}
		else if(test.front() == test2.front())
		{
			test.pop();
			test2.pop();
			while (!test.empty() && !test2.empty())
			{
				if (test.front() != test2.front())
				{
					break;
				}
				else if (test.front() == test2.front())
				{
					test.pop();
					test2.pop();
				}
			}
			if (test.empty() && test2.empty())
			{
				answer++;
				for (int i = 0; i < skill.length(); i++)
					test2.push(skill[i]);
			}
			else if (!test.empty() && test2.empty())
			{
					answer++;
					while (!test.empty())
						test.pop();
					for (int t = 0; t < skill.length(); t++)
						test2.push(skill[t]);
			}
			else if (test.empty() && !test2.empty())
			{
				answer++;
				while (!test2.empty())
					test2.pop();
				for (int t = 0; t < skill.length(); t++)
					test2.push(skill[t]);
			}
			else
			{
				while (!test2.empty())
					test2.pop();
				for (int t = 0; t < skill.length(); t++)
					test2.push(skill[t]);
				while (!test.empty())
					test.pop();
			}
		}
	}
	return answer;
}