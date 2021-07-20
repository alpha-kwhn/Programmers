#include <string>
#include <vector>

using namespace std;

int solution(int n, vector<int> lost, vector<int> reserve) {
    int answer = 0;
    vector<int> students(n, 1);
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < lost.size(); j++)
        {
            if ((i+1) == lost[j])
            {
                students[i]--;
            }
        }
    }

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < reserve.size(); j++)
        {
            if ((i+1) == reserve[j])
            {
                students[i]++;
            }
        }
    }

    for (int k = n - 1; k > 0; k--)
    {
        if ((students[k] == 2) && (students[k - 1] == 0))
        {
            students[k]--;
            students[k - 1]++;
        }
    }

    for (int i = 0; i < students.size() - 1; i++)
    {
        if ((students[i] == 2) && (students[i+1] == 0))
        {
            students[i]--;
            students[i + 1]++;
        }
    }



    for (int a = 0; a < students.size(); a++)
    {
        if (students[a] > 0)
            answer++;
    }

    return answer;
}