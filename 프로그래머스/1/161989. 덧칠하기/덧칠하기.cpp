#include <string>
#include <vector>

using namespace std;

int solution(int n, int m, vector<int> section) {
   int answer = 1;

    int current = section[0];
    for (int i = 1; i < section.size(); i++)
    {
        if (current + m > section[i])
            continue;

        current = section[i];
        answer++;
    }

    return answer;
}