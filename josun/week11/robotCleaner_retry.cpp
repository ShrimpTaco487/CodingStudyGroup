#include <iostream>
#include <vector>

using namespace std;

vector<int> dx{ -1,0,1,0 };
vector<int> dy{ 0,1,0,-1 };

vector<int> Left(int x, int y, int d) {
	vector<int> l(2, 0);
	int leftD = (d + 3) % 4;
	l[0] = x + dx[leftD];
	l[1] = y + dy[leftD];
	return l;
}

vector<int> Back(int x, int y, int d) {
	vector<int> b(2, 0);
	int BackD = (d + 2) % 4;
	b[0] = x + dx[BackD];
	b[1] = y + dy[BackD];
	return b;
}

int main() { // argv argc ? 인풋의 갯수? 인풋?
	int N, M, r, c, d;
	int map[100][100];  // 얘를 어떻게 선언해야할지 모르겠음
	scanf_s("%d %d", &N, &M);
	scanf_s("%d %d %d", &r, &c, &d);
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			scanf_s("%d", &map[i][j]);
		}
	}

	int currX = r;
	int currY = c;
	int currD = d;

	int count4 = 0;
	int countclean = 0;
	
	map[currX][currY] = 2;
	countclean ++; // clean

	while (1) {
		vector<int> l = Left(currX, currY, currD);
		if (map[l[0]][l[1]] == 0) {
			currD = (currD + 3) % 4; // turn left
			
			currX = l[0];
			currY = l[1]; // go left
			
			map[currX][currY] = 2; 
			countclean++; // clean
			count4 = 0;
		}
		else {
			currD = (currD + 3) % 4; // turn left
			count4++;
			if (count4 == 4) {
				vector<int> b = Back(currX, currY, currD);
				if (map[b[0]][b[1]] == 1) {
					count4 = 0;
					break;
				}
				else {
					currX = b[0];
					currY = b[1]; // go back
					count4 = 0;
				}
			}
		}
	}
	printf("%d", countclean);
}