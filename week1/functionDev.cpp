#include <string>
#include <vector>
#include <iostream>

using namespace std;

vector<int> solution(vector<int> progresses, vector<int> speeds) {
    vector<int> answer;
    //////////write you code here///////////
    vector<int> dayComplete;    // Completion day of each function
    for(int i=0; i<progresses.size();i++){
        int day = 1;
        while(progresses[i]<100){
            progresses[i] = progresses[i] + speeds[i];
            day++;
        }
        dayComplete.push_back(day-1);
    }
    int max = dayComplete[0];   // first element ( same as dayComplete.front() )
    int sum = 0;    // sum of completed functions
    for(int j=1; j<dayComplete.size(); j++){
        if (dayComplete[j]>max){
            answer.push_back(j-sum);
            sum = sum + answer.back();
            max = dayComplete[j];
        }
    }
    answer.push_back(dayComplete.size()-sum);
    ////////////////////////////////////////
    return answer;
}