#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

vector<int> solution(vector<int> array, vector<vector<int>> commands) {
    vector<int> answer;
    
    for(int i = 0; i < commands.size(); i++){
        vector<int> temp;
        vector<int> elem = commands[i];
        int startP = elem[0] -1;
        int endP = elem[1];
        int location = elem[2] -1;
        temp.assign(array.begin() + startP, array.begin() + endP);
        sort(temp.begin(), temp.end());
        //cout << temp.size() << "\n";
        answer.push_back(temp.at(location));
    }
    
    return answer;
}