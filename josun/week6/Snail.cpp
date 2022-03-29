#include<string>
#include<vector>
#include<iostream>
//#include<stdio.h>
#include<algorithm>
#include<math.h>

using namespace std;

vector<vector<double>> makeMatrix(vector<vector<double>> prevMatrix, int N) {
	int prevSize = prevMatrix.size();
	int currSize = prevSize + 2;
	vector<vector<double>> currMatrix(currSize, vector<double>(currSize, 0));//(pow(currSize,2));
	
	for (int i = 0; i < prevSize; i++) {
		for (int j = 0; j < prevSize; j++) {
			currMatrix[i + 1][j + 1] = prevMatrix[i][j];
		}
	}

	for (int k = 0; k < currSize - 1; k++) {
		currMatrix[k][0] = pow(currSize, 2) - k;
		currMatrix[currSize - 1][k] = pow(currSize, 2) - currSize + 1 - k;
		currMatrix[currSize - 1 - k][currSize - 1] = pow(currSize, 2) - 2*currSize +2 - k;
		currMatrix[0][currSize - 1 - k] = pow(currSize, 2) - 3*currSize +3 - k;
	}

	if (currSize == N) {
		return currMatrix;
	}
	else {
		return makeMatrix(currMatrix, N);
	}
}

vector<int> location(vector<vector<double>> vectorN, int k) {
	vector<int> answer2(2, 0);
	int range = 0;
	int N = vectorN.size();
	//printf("N: %d \n", N);

	for (int i = 0; i < N / 2; i++) {
		if (k > vectorN[i][i]) {
			range = i-1;
			break;
		}
	}
	//printf("range: %d \n", range);
	int diff = vectorN[range][range] - k;
	//printf("diff: %d \n", diff);
	int mox = diff / (N - 1);
	int nmj = diff % (N - 1);
	//printf("mox: %d, nmj: %d \n", mox, nmj);

	if (mox==0) {
		//printf("case 1\n");
		answer2[0] = nmj + range + 1;
		answer2[1] = range + 1;
	}
	else if (mox==1) {
		//printf("case 2\n");
		answer2[0] = N - range;
		answer2[1] = nmj + range + 1;
	}
	else if (mox==2) {
		//printf("case 3\n");
		answer2[0] = N + range - nmj;
		answer2[1] = N - range;
	}
	else if (mox == 3) {
		//printf("case 4\n");
		answer2[0] = range + 1;
		answer2[1] = N - range - nmj;
	}
	else {
		//printf("error!\n");
	}
	return answer2;
}

int main() {
	int N;
	int k;
	scanf_s("%d %d", &N, &k);
	vector<vector<double>> initialMatrix(1,vector<double>(1,0));
	initialMatrix[0][0] = 1;
	vector<vector<double>> answer1 = makeMatrix(initialMatrix,N);
	vector<int> answer2 = location(answer1, k);

	for (int i = 0; i < answer1.size(); i++) {
		for (int j = 0; j < answer1.size(); j++) {
			printf("%.0f ", answer1[i][j]);
		}
		printf("\n");
	}

	printf("%d %d", answer2[0], answer2[1]);
	
	return 0;
}