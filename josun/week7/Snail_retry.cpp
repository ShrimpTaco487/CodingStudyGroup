#include<iostream>
#include<vector>
#include<algorithm>
#include<math.h>

using namespace std;

int main() {
	int N;
	int num;
	scanf_s("%d %d", &N, &num);

	vector<vector<int>> matrix(N, vector<int>(N, 0));
	vector<vector<bool>> visited(N, vector<bool>(N, false));

	int startnum = N * N;
	vector<vector<int>> direction{ {1,0},{0,1},{-1,0},{0,-1} };
	int x = 0;
	int y = 0;
	int curr = 0;
	int locx = 0;
	int locy = 0;

	for (int k = startnum; k > 0; k--) {
		matrix[x][y] = k;
		visited[x][y] = true;
		if (k == num) {
			locx = x + 1;
			locy = y + 1;
		}
		int nextx = x + direction[curr % 4][0];
		int nexty = y + direction[curr % 4][1];
		if ((nextx < 0) || (nexty < 0) || (nextx >= N) || (nexty >= N) || visited[nextx][nexty] == true) {
			curr += 1;
		}
		x += direction[curr % 4][0];
		y += direction[curr % 4][1];
	}

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			printf("%d ", matrix[i][j]);
		}
		printf("\n");
	}
	printf("%d %d", locx, locy);
	
	return 0;
}