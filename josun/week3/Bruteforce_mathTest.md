- 각각 찍은거랑 답이랑 일일히 비교... & 맞았을 때 마다 score++

- 문제 수보다 찍는 array가 더 짧으면 안되니까 뒤로 push_back해서 추가하기
    - 문제 수랑 비교해서 그거보다 짧을때만?
    - 그냥 생각 안하고 매번?

- 가장 많은 문제를 맞힌 사람 return
    - max값 찾기? 그럼 동점자 처리를 어떻게하지
    - algorithm 라이브러리의 `max_element`: vector에서 가장 큰 값을 가지는 index를 return
        - `max_element(v.begin(), v.end())` 이런 식으로 사용
        - 동점자는 return이 안됨 (제일 앞의 index 하나만 return) --> 못쓰겠다
    - 걍 각각 점수를 1:1로 다 비교해서... 한 번도 진적 없으면 (늘 다른 애들 보다 크거나 같았던) push_back?
    대충...
    for(int j = 0부터 끝까지){
        if(jth < 다른애){
            break;
        }
        else{
            count++;
        }
    }
    if(count == score.size()){
        push_back(j+1);
    }
