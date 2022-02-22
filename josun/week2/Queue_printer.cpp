#include <string>
#include <vector>
#include <iostream>

using namespace std;

#include <string>
#include <vector>
#include <iostream>

using namespace std;

int solution(vector<int> priorities, int location) {
    int answer = 0;
    /////////////write your code here//////////////
    for(int loop = 0 ; loop<100; loop++){ // while로 하려고 했는데 애초에 loc == 0 이면 실행이 안됨
        int notMax = 0;
        for (int i=1; i<priorities.size(); i++){
            if (priorities[0]<priorities[i]){
                notMax++;
            }
        }
        if (notMax){
            cout << "notMax: " << priorities[0] <<"\n"; 
            priorities.push_back(priorities[0]);
            if (location==0){
                location = priorities.size(); // 아 왜 size로 못하냐고! location을 맨 끝으로 하고싶은데 end back은 아니고 size는 일케 못쓴대
            }
        }
        else{
            cout << "Max: " << priorities[0] <<"\n";
            location--;
            answer++;
        }
        priorities.erase(priorities.begin());
        cout << "loc: " << location << "\n";
        cout << "ans: " << answer << "\n";
        if (location<0){
            break;
        }
    }
    ///////////////////////////////////////////////
    return answer;
}

int main(){
    vector<int> priorities = {1,1,9,1,1,1} ;
    int location = 0;
    solution(priorities, location);
    return 0;
}