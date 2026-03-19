#include <string>
#include <map>
#include <vector>
#include <iostream>

using namespace std;

void enqueue(int num, vector<int>& minHeap, vector<int>& maxHeap)
{
    minHeap.push_back(num);
    int posMin = minHeap.size() - 1;
    while (posMin > 0)
    {
        int upPos = (posMin - 1) / 2;
        if (minHeap[posMin] < minHeap[upPos])
        {
            int temp = minHeap[posMin];
            minHeap[posMin] = minHeap[upPos];
            minHeap[upPos] = temp;

            posMin = upPos;
        }
        else
            break;
        
    }

    maxHeap.push_back(num);
    int posMax = maxHeap.size() - 1;
    while (posMax > 0)
    {
        int upPos = (posMax - 1) / 2;
        if (maxHeap[posMax] > maxHeap[upPos])
        {
            int temp = maxHeap[posMax];
            maxHeap[posMax] = maxHeap[upPos];
            maxHeap[upPos] = temp;

            posMax = upPos;
        }
        else
            break;
    }

    return ;
}

void rebuildMin(vector<int>& minHeap)
{
    int pos = 0;
    while (true)
    {
        if (pos * 2 + 1 > minHeap.size() - 1)
            break;

        if (pos * 2 + 2 == minHeap.size())
        {
            if (minHeap[pos * 2 + 1] < minHeap[pos])
            {
                int temp = minHeap[pos];
                minHeap[pos] = minHeap[pos * 2 + 1];
                minHeap[pos * 2 + 1] = temp;
            }
            break;
        }
        else
        {
            if (minHeap[pos] <= minHeap[pos*2 + 1] && minHeap[pos] <= minHeap[pos*2 + 2])
                break;

            int next;
            if (minHeap[pos * 2 + 1] >= minHeap[pos] && minHeap[pos] > minHeap[pos*2 + 2])
                next = pos * 2 + 2;
            else if (minHeap[pos * 2 + 1] < minHeap[pos] && minHeap[pos] <= minHeap[pos*2 + 2])
                next = pos * 2 + 1;
            else
                next = pos * 2 + (minHeap[pos * 2 + 1] < minHeap[pos*2 + 2] ? 1 : 2);

            int temp = minHeap[pos];
            minHeap[pos] = minHeap[next];
            minHeap[next] = temp;

            pos = next;
        }
    }
}

void checkDeletedMin(vector<int>& minHeap, map<int, int>& deleted)
{
    while (deleted[minHeap[0]] > 0)
    {
        deleted[minHeap[0]] -= 1;
        if (deleted[minHeap[0]] == 0)
            deleted.erase(minHeap[0]);

        minHeap[0] = minHeap[minHeap.size() - 1];
        minHeap.pop_back();

        if (minHeap.size() == 0)
            break;

        rebuildMin(minHeap);
    }
}

int dequeueMin(vector<int>& minHeap, map<int, int>& deleted) 
{
    int minNum = minHeap[0];
    minHeap[0] = minHeap[minHeap.size() - 1];
    minHeap.pop_back();

    if (deleted[minNum] == 0)
        deleted[minNum] = 1;
    else    
        deleted[minNum] += 1;

    if (minHeap.size() > 0)
        rebuildMin(minHeap);

    return minNum;
}

void rebuildMax(vector<int>& maxHeap)
{
    int pos = 0;

    while (true)
    {
        if (pos * 2 + 1 > maxHeap.size() - 1)
            break;

        if (pos * 2 + 2 == maxHeap.size())
        {
            if (maxHeap[pos * 2 + 1] > maxHeap[pos])
            {
                int temp = maxHeap[pos];
                maxHeap[pos] = maxHeap[pos * 2 + 1];
                maxHeap[pos * 2 + 1] = temp;
            }
            break;
        }
        else
        {
            if (maxHeap[pos] >= maxHeap[pos*2 + 1] && maxHeap[pos] >= maxHeap[pos*2 + 2])
                break;
            int next;
            if (maxHeap[pos * 2 + 1] <= maxHeap[pos] && maxHeap[pos] < maxHeap[pos*2 + 2])
                next = pos * 2 + 2;
            else if (maxHeap[pos * 2 + 1] > maxHeap[pos] && maxHeap[pos] >= maxHeap[pos*2 + 2])
                next = pos * 2 + 1;
            else
                next = pos * 2 + (maxHeap[pos * 2 + 1] > maxHeap[pos*2 + 2] ? 1 : 2);

            int temp = maxHeap[pos];
            maxHeap[pos] = maxHeap[next];
            maxHeap[next] = temp;

            pos = next;
        }
    }
}

void checkDeletedMax(vector<int>& maxHeap, map<int, int>& deleted)
{
    while (deleted[maxHeap[0]] > 0)
    {
        deleted[maxHeap[0]] -= 1;
        if (deleted[maxHeap[0]] == 0)
            deleted.erase(maxHeap[0]);

        maxHeap[0] = maxHeap[maxHeap.size() - 1];
        maxHeap.pop_back();

        if (maxHeap.size() == 0)
            break;

        rebuildMax(maxHeap);
    }
}

int dequeueMax(vector<int>& maxHeap, map<int, int>& deleted)
{
    int maxNum = maxHeap[0];
    maxHeap[0] = maxHeap[maxHeap.size() - 1];
    maxHeap.pop_back();

    if(deleted[maxNum] == 0)
        deleted[maxNum] = 1;
    else
        deleted[maxNum] += 1;

    if (maxHeap.size() > 0)
        rebuildMax(maxHeap);

    return maxNum;
}

vector<int> solution(vector<string> operations) {
    vector<int> answer;
    
    vector<int> minHeap;
    vector<int> maxHeap;

    map<int, int> deletedMin;
    map<int, int> deletedMax;

    // cout << " -----------------------------\n" << endl;

    for (auto command : operations)
    {
        // cout << command << endl;

        if (command[0] == 'D')
        {
            bool isMinDequeue = command[2] == '-';

            if (isMinDequeue && minHeap.size() > 0)
            {
                checkDeletedMin(minHeap, deletedMin);
            
                if (minHeap.size() > 0)
                    dequeueMin(minHeap, deletedMax);
            }
            else if (!isMinDequeue && maxHeap.size() > 0)
            {
                checkDeletedMax(maxHeap, deletedMax);

                if (maxHeap.size() > 0) 
                    dequeueMax(maxHeap, deletedMin);
            }
        }
        else if (command[0] == 'I')
        {
            auto number = stoi(command.substr(2));
            
            enqueue(number, minHeap, maxHeap);
        }

        // for (auto num : minHeap)
        //     cout << num << ' ';
        // cout << '\n';

        // for (auto num : maxHeap)
        //     cout << num << ' ';
        // cout << '\n';
    }

    if (minHeap.size() == 0 || maxHeap.size() == 0)
        return {0, 0};

    checkDeletedMin(minHeap, deletedMin);
    checkDeletedMax(maxHeap, deletedMax);

    if (minHeap.size() > 0 && maxHeap.size() > 0)
    {
        int resultMin = dequeueMin(minHeap, deletedMax);
        int resultMax = dequeueMax(maxHeap, deletedMin);

        answer.push_back(resultMax);
        answer.push_back(resultMin);
    }
    else
        answer = {0, 0};

    return answer;
}

// int main()
// {
//     vector<string> operations = { "I 10", "I 20", "D 1", "I 30", "I 40", "D -1", "D -1" };
//     auto result = solution(operations);

//     for (auto num : result)
//         cout << num << ' ';
//     cout << '\n';

//     vector<string> operations2 = {"I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"};
//     auto result2 = solution(operations2);
    
//     for (auto num : result2)
//         cout << num << ' ';
//     cout << '\n';

//     vector<string> operations3 = {"I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"};
//     auto result3 = solution(operations3);

//     for (auto num : result3)
//         cout << num << ' ';
//     cout << '\n';

//     vector<string> operations4 = {"I 40", "I 50", "I 40", "D -1", "D -1"};
//     auto result4 = solution(operations4);

//     for (auto num : result4)
//         cout << num << ' ';
//     cout << '\n';

//     return 0;
// }