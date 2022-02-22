priorities가 높은 애부터 출력댐
자기보다 큰게 하나라도 남아있으면 맨 뒤로
위치가 계속 바뀌기 때문에 내가 원하는 애의 위치 tracking을 해줘야됨

[2, 1, 3, 2], 2
1

2 1 3 2 / 2

비교 비교... 
    0보다 큰게 있다 ->
        0 맨뒤로
        if 0이 나였으면 location = 맨뒤
    0이 제일 크다 ->
        location -- / answer++
erase

location이 음수면 그만하기?


??? 아 왜 location = priorities.size(); 이거 절대 안되지 맨 뒤 index로 location 바꾸고 싶다고!!!
signal: segmentation fault (core dumped) // 죽어도 이런 에러가..

//검색해보니
대표적
    1. 배열 잘못써서 (범위를 초과, 음수 인덱스 참조)
    2. 포인터 잘못써서


고급지게-위키피디아 왈
    세그멘테이션 결함은 
    프로그램이 허용되지 않은 메모리 영역에 접근을 시도하거나, 
    허용되지 않은 방법으로 메모리 영역에 접근을 시도할 경우 발생한다.