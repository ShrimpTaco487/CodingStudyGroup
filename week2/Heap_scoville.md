일단 정렬을 해용 작은 순으로 (어케함 min부터 pop_back해봐?) // sort 함수가 있음

while(scoville[0]<K){ // 젤 작은게(index 0인 애) K 이상이 되면 그만하기
min1 = scoville[0];
min2 = scoville[1];
scoville.erase(0,2); // 첫번째 두번째를 지우고
new = min1 + min2 * 2 // new 계산
for (vector i th 원소에 대해서){
if (scoville[i]<new){  // heap처럼 만들려고 i번째 애랑 크기 비교... 
아무것도 안함
}
else{
scoville.insert(i,new) //i번째 자리에 new를 넣어
break;
}
}
answer++;
}