#include <string>
#include <vector>
#include <bitset>
using namespace std;

vector<string> solution(int n, vector<int> arr1, vector<int> arr2) {
    vector<string> answer;
    vector<string> repos, depos;
    string nae;
    for (int i = 0; i < arr1.size(); i++)
        repos.push_back(bitset<16>(arr1[i]).to_string());
    for (int a = 0; a < arr2.size(); a++)
        depos.push_back(bitset<16>(arr2[a]).to_string());

    for (int j = 0; j < n; j++)
    {
        for (int m = 16-n; m < 16; m++)
        {
            if ((repos[j][m] == '0') && (depos[j][m] == '0'))
                nae = nae + " ";
            else
                nae = nae + "#";
        }
        answer.push_back(nae);
        nae = "";
    }
    return answer;
}
