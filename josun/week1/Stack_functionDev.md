스택이 뭐고 큐가 뭔데...

그딴거 모르는 상태에서 다짜고짜 덤벼보겠음

```c++
progresses + speeds * day (day: from 1 to 99)하는데
계속 더하다가....
progress의 첫번째  entity가 100이상이 돼
그럼 entity를 첨부터 쭉 뒤로 훑다가 100보다 작은애가 나오면 stop
그 전까지를 다 pop? --> answer[1]은 요 entity 갯수
그러고 다시 반복...
또 pop되면 answer[2]는 그 entity 갯수...

//vector<int> progNew;
    
    for (int day = 1; day<100; day++){
        progresses = progresses + speeds; //element wise sum이 안되네
        for (int idx = 1; idx <= progresses.size; idx++){
            if (progresses[idx] < 99){
                answer.push_back = idx;
            }
        }
    }
```

***
아니면...
                                      
100 될때까지 element를 각각 더해가면서 날짜수를 세면
```
[7,3,9]
[5,10,1,1,20,1]
```
맨 앞 entity를 max로하고, 뒤에 애들이랑 비교해서 더 큰 수가 나올 때 까지...
                                      
더 큰 수 나오면 걔가 max, 걔의 index를 answer.back_push()

이걸 연속해서...

answer에 먼저 들어가있는 애들의 합을 push해야된다. (index에서 지금까지 들어가 있는 애들을 빼야 그날 release되는 기능 수): index - sum

```c++
vector<int> dayv
int day=1;
for i from 1 to progresses.size()
    while (progresses[i]<100){
        progresses[i] = progresses[i] + day;
        day++;
  }
  dayv.back_push(day);
```
