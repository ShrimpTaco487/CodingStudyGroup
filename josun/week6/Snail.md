[0][0]은 항상 N의 제곱 -> 뒤에서부터 생각하면 될듯

숫자 위치 찾는건 탐색을 해야할것 같아 BFS!

***
테두리를 만들어?

### <왼쪽줄>
```
[0][0] = N^2

[1][0] = N^2-1

[2][0] = N^2-2

...

[N-2][0] = N^2-(N-2)

--> for i=0부터 N-2까지 [i][0] = N^2-i
```
### < 아랫줄>
```
[N-1][0] = N^2-(N-1)

[N-1][1] = N^2-N

[N-1][2] = N^2-(N+1)

[N-1][3] = N^2-(N+2)

...

[N-1][N-2] = N^2-(N+4)

--> for i=0부터 N-2까지 [N-1][i] = N^2-N+1-i
```
### <오른쪽줄>
```
[1][N-1] = N^2-N-5 = N^2-N-(N-2) 

[2]]N-1] = N^2-N-(N-3)

...

[N-2][N-1] = 

[N-1][N-1] = 

--> for i=0부터 N-2까지 [i+1][N-1] = 
```
### <윗줄>
```
[0][1] = 

[0][2] = 

[0][3] = 

...

[0][N-1] = 

--> for i=0부터 N-2까지 [0][i+1] = 
```

근데 이렇게하면 10분안에 못풀잖어ㅡㅡ

***
재귀함수
N * N 행렬 만드는 함수 makeMatrix 라고 하면

```c++
makeMatrix(prevMatrix)
    currMatrix(i+1)(j+1) = prevMatrix(i,j)    //행,열 1칸씩 shift

    for k = 0부터 N-2까지
        [k][0] = N제곱 - k
    for k = 0부터 N-2까지
        [N-1][k] = [N-2][0] - k
    for k = 0부터 N-2까지
        [N-1-k][N-1] = [N-1][N-2] - k
    for k = 0부터 N-2까지
        [0][N-1-k] = [0][N-1] -k
```

***
재귀함수는 memory 효율이 나쁨 (매 재귀함수 호출마다 memory를 계속 추가 할당)

**'메모리 초과'** 로 실패
