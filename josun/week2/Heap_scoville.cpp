#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<int> scoville, int K) {
    int answer = 0;
    int min1 = 0;
    int min2 = 0;
    int newscv = 0;
    sort(scoville.begin(), scoville.end());//정렬
    while(scoville[0]<K){ //젤 작은게(0) K 이상이 되면 그만하기
        if (scoville.size()<2){
            answer=-1;
            break;
        }
        min1 = scoville[0];
        min2 = scoville[1];
        scoville.erase(scoville.begin()+0, scoville.begin()+2);
        //scoville.erase(scoville.begin()+0);
        newscv = min1 + min2 * 2;
        for (int i=0; i<scoville.size(); i++){
            if (scoville[i]>=newscv){
                scoville.insert(scoville.begin()+i,newscv);
                break;
            }
        }
        if (scoville.back()<newscv){
            scoville.push_back(newscv);
        }
        answer++;
    }
    return answer;
}