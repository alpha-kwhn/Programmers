
#include<string>
#include<vector>
#include<queue>
using namespace std;

vector<int>solution(vector<int> progresses, vector<int> speeds)
{
	vector<int>answer;
	int check = 0; //당장 완료되야 하는 우선적인 작업이 100%완료 되는 그 순간, 더불어 끝낼 수 있는 작업의 총 갯수
	int loop = 0; //당장 완료가 되어야 하는 우선 적인 작업의 index를 나타냄, 한 작업이 끝날 때마다 1씩 증가
	int count = 0; //개발이 완료된 작업들의 누적량 -> 더 이상의 작업진행 여부 결정(while문)
	queue<int> factory;

	while (count != progresses.size())
	{
		for (int i = loop; i < progresses.size(); i++)
			progresses[i] += speeds[i];
		for (int j = loop; j < progresses.size(); j++)
			factory.push(progresses[j]);
		if (factory.front() < 100)
		{
			while (!factory.empty())
				factory.pop();
		}
		else if (factory.front() >= 100)
		{
			while ((factory.front() >= 100) && (!factory.empty()))
			{
				check++;
				loop++;
				count++;
				factory.pop();
			}
			while (!factory.empty())
				factory.pop();
			answer.push_back(check);
			check = 0;
		}
	}
	return answer;
}