#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

int solution(vector<int> people, int limit) {
	int answer = 0;
	sort(people.begin(), people.end()); // 오름차순 정렬
	int count = 0;

	while (people.size() > count)
	{
		int tmp = people.back();
		people.pop_back();
		//제일 큰 값 + 제일 작은 값 조합을 계속 찾아나감(greedy)
		if (tmp + people[count] <= limit)
		{
			++answer;
			++count;
		}
		else //둘 중 한 명만 태우는 경우
			++answer;
	}
	return answer;
}