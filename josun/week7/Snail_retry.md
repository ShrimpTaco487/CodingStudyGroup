**@kimcando 의 지난주 풀이 방법 참고함**

***
[0][0]은 N의 제곱 - 여기서부터 시작해서 역순으로 채우기

DFS, BFS 처럼 bool 형식의 visited를 두고 방문했으면 true, 아니면 false 

이동 방향은 '아래로 -> 오른쪽으로 -> 위로 -> 왼쪽으로' 반복
    현재방향 % 4 해서 반복되도록

방향 전환해야 하는 시점 (다 or 조건)
* 다음 칸이 N*N 행렬 범위를 넘어갈 때
    - 0보다 작거나 
    - N보다 크거나 같을 때
* 다음 칸이 이미 방문 (true) 일때