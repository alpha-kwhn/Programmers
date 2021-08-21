#include<vector>
#include<string>
#include<iostream>
#include<queue>
using namespace std;

int solution(int bridge_length, int weight, vector<int> truck_weights)
{
	int answer = 0;
	int index = 0;
	int sum = 0;
	int tmp = 0;
	int zero = 0;
	queue<int>bridge;

	while (1)
	{
		if (truck_weights.empty())
		{
			answer += bridge_length;
			while (!bridge.empty())
				bridge.pop();
			break;
		}
		else
		{
			if ((sum + truck_weights[index] > weight) && (bridge.size() != bridge_length))
			{
				bridge.push(zero);
				answer++;
			}
			else if ((sum + truck_weights[index] > weight) && (bridge.size() == bridge_length))
			{
				tmp = bridge.front();
				sum -= tmp;
				bridge.pop();
				if (sum + truck_weights[index] > weight)
					bridge.push(zero);
				else
				{
					bridge.push(truck_weights[index]);
					sum += truck_weights[index];
					truck_weights.erase(truck_weights.begin());
				}
				answer++;
			}
			else if ((sum + truck_weights[index] <= weight) && (bridge.size() == bridge_length))
			{
				tmp = bridge.front();
				sum -= tmp;
				bridge.pop();
				bridge.push(truck_weights[index]);
				sum += truck_weights[index];
				truck_weights.erase(truck_weights.begin());
				answer++;
			}
			else if ((sum + truck_weights[index] <= weight) && (bridge.size() != bridge_length))
			{
				bridge.push(truck_weights[index]);
				sum += truck_weights[index];
				truck_weights.erase(truck_weights.begin());
				answer++;
			}
		}
	}
	return answer;
}