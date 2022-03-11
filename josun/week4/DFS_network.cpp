#include <string>
#include <vector>
#include <iostream>
//#include <stack>

using namespace std;

int solution(int n, vector<vector<int>> computers) {
    int answer = 0;
    
    vector<bool> visited(n,false);
    vector<int> mem;
    
    for(int i = 0; i<n; i++){
        if(!visited[i]){
            int current = i;
            mem.push_back(i);
            visited[current] = true;
            while(mem.size() != 0){
                current = mem.back();
                mem.pop_back();
                for(int j = 0; j<n; j++){
                    if(computers[current][j] != 0 && !visited[j]){
                        mem.push_back(j);
                        visited[j] = true;
                    }
                }
            }
            answer++;
        }
    }
    
    return answer;
}