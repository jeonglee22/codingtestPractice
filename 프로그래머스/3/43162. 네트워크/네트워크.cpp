#include <string>
#include <vector>
#include <iostream>

using namespace std;

int solution(int n, vector<vector<int>> computers) {
    int answer = 0;

    vector<bool> checked = vector<bool>(n, false);
    int pos = 0;

    while (n > 0)
    {
        vector<int> comStack = vector<int>();

        while (checked[pos])
            pos++;

        comStack.push_back(pos);
        checked[pos] = true;
        n--;

        while (comStack.size() > 0)
        {
            int current = comStack[0];
            comStack.erase(comStack.begin());

            vector<int> connects = computers[current];
            for (int i = 0; i < connects.size(); i++)
            {
                if (i == current)
                    continue;

                if (checked[i])
                    continue;

                if (connects[i] == 0)
                    continue;

                comStack.push_back(i);
                checked[i] = true;
                n--;
            }
        }

        answer++;
    }

    return answer;
}