#include <iostream>
#include <string>
#include <vector>

using namespace std;

int solution(int n, int w, int num) {
    int answer = 0;
    
    int blocks = (n - num) / (w * 2);
    
    answer += blocks * 2;
    
    n -= blocks * (w*2);
    
    if ( n >= num) answer++;
    if ( n >= num + 2 * ( (w - 1) - (num - 1) % w ) + 1) answer++;
    
    return answer;
}
