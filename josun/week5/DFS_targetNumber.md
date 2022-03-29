전체 그래프를 다 들를거면(모든 경우의 수를 다 볼거면) DFS BFS 상관없대

BFS로 해보고싶은데 DFS밖에 모르겠음 둘다 해보자

그래프를 어떻게 구현해야할지? 몇번 노드를 몇으로 해서?

***
[a,b] 라고 치면 노드 수 1+2+4, depth 3 짜리
```
0 - 0+a - 0+a+b
         \0+a-b
    0-a - 0-a+b
         \0-a-b
```
이런식으로?

노드가...

[0, 0] [1,a] [2,-a] 이런식으로도 할수있남?

***
아 니 면

재귀로 풀기


어찌됐든 완전이진트리 인거잖음

(트리를 먼저 만들어야되나?)
```c++
int sum = 0;
int depth = 0;
dfs(numbers, sum, depth, indicator, target){
    (어떤 노드에 대해서)
    depth++;
    sum = sum + numbers[depth] * indicator;
    if (depth == numbers.size() && sum == target)
        answer++;
    dfs(numbers, sum, depth, 1, target);
    dfs(numbers, sum, depth, -1, target);
}
```
answer도 input으로 받아야된다...
