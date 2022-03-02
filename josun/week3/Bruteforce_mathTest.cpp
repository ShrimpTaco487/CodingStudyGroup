#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> answers) {
    vector<int> answer;
    
    vector<int> SPJ1{1, 2, 3, 4, 5};
    vector<int> SPJ2{2, 1, 2, 3, 2, 4, 2, 5};
    vector<int> SPJ3{3, 3, 1, 1, 2, 2, 4, 4, 5, 5};
    
    vector<int> score(3,0);
    
    for(int i = 0; i < answers.size(); i++){
        if(SPJ1[i]==answers[i]){
            score[0]++;
        }
        if(SPJ2[i]==answers[i]){
            score[1]++;
        }
        if(SPJ3[i]==answers[i]){
            score[2]++;
        }
        SPJ1.push_back(SPJ1[i]);
        SPJ2.push_back(SPJ2[i]);
        SPJ3.push_back(SPJ3[i]);
    }
    //cout << "전체: " << score[0] << " " << score[1] << " " << score[2] << "\n";
    for(int j = 0; j<score.size(); j++){
        int count = 0;
        for(int k = 0; k<score.size(); k++){
            if(score[j]<score[k]){
                break;
            }
            else{
                count++;
            }
            if(count==score.size()){
                answer.push_back(j+1);
            }
        }
        
    }
    
    return answer;
}