#include <iostream>
#include <vector>
#include <math.h>
#include <algorithm>
#include <stdio.h>

using namespace std;

vector<vector<bool>> map(101, vector<bool>(101, false));
vector<int> dx{1, 0, -1, 0};
vector<int> dy{0, -1, 0, 1};

// 0: 0
// 1: 0 1
// 2: 0 1 2 1
// 3: 0 1 2 1 2 3 2 1
// 4: 0 1 2 1 2 3 2 1 2 3 0 3 2 3 2 1
// 이동횟수: 2^g, 이동방향: 이전 방향 벡터로 저장 -> 순서 뒤집어서 1씩 더해서 append

void visitXYs(int x, int y, int g, int depth, vector<int> dir) {
	vector<int> ori_dir = dir;
	depth++;
	while (!ori_dir.empty()) {
		int curr_dir = (ori_dir.back() + 1) % 4;
		ori_dir.pop_back();
		x = x + dx[curr_dir];
		y = y + dy[curr_dir];
		map[x][y] = true;
		//printf("x: %d, y: %d\n", x, y); // ERASE
		dir.push_back(curr_dir);
	}
	if (depth < g) {
		visitXYs(x, y, g, depth, dir);
	}
}

int main() {
	int answer = 0;
	int N, I;
	vector<vector<int>> arr(20, vector<int>(4, 0));
	scanf_s("%d", &N);
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < 4; j++) {
			scanf_s("%d", &I);
			arr[i][j] = I;
		}
	}

	for (int k = 0; k < N; k++) {
		int x = arr[k][0];
		int y = arr[k][1];
		int d = arr[k][2];
		int g = arr[k][3];
		map[x][y] = true;
		//printf("x: %d, y: %d\n", x, y); // ERASE
		x = x + dx[d];
		y = y + dy[d];
		map[x][y] = true;
		//printf("x: %d, y: %d\n", x, y); // ERASE
		vector<int> dir{ d };
		int depth = 0;
		if (g!=depth) {
			//printf("g: %d, depth: %d\n", g, depth);  // ERASE
			visitXYs(x, y, g, depth, dir);
		}
	}
	//printf("\n**answer**\n");  // ERASE
	for (int n = 0; n < 100; n++) {
		for (int m = 0; m < 100; m++) {
			if (map[n][m] && map[n + 1][m] && map[n][m + 1] && map[n + 1][m + 1]) {
				//printf("n: %d, m: %d\n", n, m);  // ERASE
				answer++;
			}
		}
	}
	printf("%d", answer);
}