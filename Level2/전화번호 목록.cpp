#include <string>
#include <vector>

using namespace std;

bool solution(vector<string> phone_book) {
    bool answer = true;
    int size = phone_book.size();
    for (int i = 0; i < size; i++)
    {
        for (int j = 0; j < size; j++)
        {
            if (i != j)
            {
                if ((phone_book[j].find(phone_book[i]) != string::npos))
                {
                    int tmp = phone_book[i].size();
                    string k;
                    k.assign(phone_book[j], 0, tmp);
                    if ((k == phone_book[i]))
                        return false;
                }
            }
        }
    }
    return answer;
}