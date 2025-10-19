#include <string>
#include <vector>

using namespace std;

int solution(int k, int m, vector<int> score) {
    int answer = 0;

    vector<int> costs = vector<int>(k);

    for (int i = 0; i < score.size(); i++)
    {
        costs[score[i] - 1]++;
    }

    int boxSize = m;
    int pos = costs.size() - 1;
    while (pos >= 0)
    {
        int value = costs[pos];
        if (value >= boxSize)
        {
            costs[pos] -= boxSize;
            answer += (pos + 1) * m;

            boxSize = m;
        }
        else
        {
            pos--;
            boxSize -= value;
        }
    }

    return answer;
}