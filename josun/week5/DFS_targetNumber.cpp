#include <string>
#include <vector>
#include <iostream>

using namespace std;

int dfs(vector<int> numbers, int sum, int depth, int indicator, int target, int answer) {
    sum = sum + numbers[depth] * indicator;
    ++depth;
    if (depth == numbers.size()){
        if (sum == target){
            answer++;
        }
    }
    else{
        int answer1 = dfs(numbers, sum, depth, 1, target, answer);
        int answer2 = dfs(numbers, sum, depth, -1, target, answer);
        answer = answer1 + answer2;
    }
    return answer;
}

int solution(vector<int> numbers, int target) {
    int answer = 0;
    
    int answer1 = dfs(numbers, 0, 0, 1, target, answer);
    int answer2 = dfs(numbers, 0, 0, -1, target, answer);
    
    answer = answer1 + answer2;
    
    return answer;
}