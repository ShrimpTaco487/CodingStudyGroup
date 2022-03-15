#include<iostream>
#include<vector>
#include<stack>

using namespace std;

int V_size = 5;

vector<vector<int>> adjacent = {
    {0,1,1,0,0},
    {1,0,1,1,0},
    {1,1,0,0,0},
    {0,1,0,0,0},
    {0,0,0,0,0}
};

vector<bool> visited(V_size, false);
stack<int> mem;

void dfs(int start){
    int current = start;
    mem.push(current);
    visited[current] = true;
    while(mem.size()!=0){
        current = mem.top();
        mem.pop();
        cout << "Visit: " << current << "\n";
        for(int i = 0; i < V_size; i++){
            if(adjacent[current][i] != 0 && !visited[i]){
                current = i;
                mem.push(current);
                visited[current] = true;
            }
        } 
    }
}

void dfsAll(){
    visited = vector<bool>(adjacent.size(), false);
    for(int i = 0; i < adjacent.size(); i++){
        if(!visited[i]) dfs(i);
    }
}

void main(){
    dfsAll();
}