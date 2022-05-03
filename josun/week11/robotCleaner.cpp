#include <iostream>
#include <vector>
#include <algorithm>
#include <math.h>

using namespace std;

// 방향을 이런식으로 말고
// dx{-1, 0, 1, 0}
// dy{0, 1, 0, -1}
// 이런식으로 해서...

vector<int> Left(int x, int y, int d) {
	vector<int> l(2, 0);
	l[0] = x;
	l[1] = y;

	switch (d)
	{
	case 0:
		l[1]--;
		break;
	case 1:
		l[0]--;
		break;
	case 2:
		l[1]++;
		break;
	case 3:
		l[0]++;
	}
	return l;
}

vector<int> Back(int x, int y, int d) {
	vector<int> b(2, 0);
	b[0] = x;
	b[1] = y;

	switch (d)
	{
	case 0:
		b[0]++;
		break;
	case 1:
		b[1]--;
		break;
	case 2:
		b[0]--;
		break;
	case 3:
		b[1]++;
	}
	return b;
}

int main() {
	int N;
	int M;
	int r;
	int c;
	int d;
	int map[100][100];

	scanf_s("%d %d", &N, &M);
	scanf_s("%d %d %d", &r, &c, &d);
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			scanf_s("%d", &map[i][j]); //vector input?
		}
	}

	int currX = r;
	int currY = c;
	int currD = d;
	
	int count4 = 0;  // 2a count
	int countclean = 0;

	map[currX][currY] = 2;  // 1 (청소), '청소' ==2
	countclean++;
	while (1) {
		//printf("curr X: %d, Y: %d, dir: %d \n", currX, currY, currD);
		vector<int> l = Left(currX, currY, currD);
		//printf("left X: %d, Y: %d, map[leftX][leftY]: %d \n", l[0], l[1], map[l[0]][l[1]]);
		if (map[l[0]][l[1]] == 0) {  // 2a-1, '청소를 하지 않은 빈공간'==0
			currD = (currD + 3) % 4; //회전
			currX = l[0];
			currY = l[1]; //이동
			map[currX][currY] = 2;  // 1 (청소), '청소'==2
			countclean++;
			count4 = 0;
		}
		else {  // 2a-2
			currD = (currD + 3) % 4; // 회전
			count4++;
			if (count4 == 4) {  // 2b (하나 밖에? 여기에?)
				count4 = 0;
				vector<int> b = Back(currX, currY, currD);
				if (map[b[0]][b[1]] == 1) {  // 2b-1, '벽'==1
					break;  // 멈춘다
				}
				else {  // 2b-2
					currX = b[0];
					currY = b[1];  // 후진
				}
			}
		}
	}

	printf("%d", countclean);
}