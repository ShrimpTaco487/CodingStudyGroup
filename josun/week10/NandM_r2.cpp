#include <iostream>
#include <vector>

using namespace std;

//int sum = 0;

int printV(vector<int> v) {
	for (int k = 0; k < v.size(); k++) {
		printf("%d ", v[k]);
	}
	printf("\n");
	return 0;
}

int solution(int i, int N, int M, vector<int> answer, vector<bool> visited) {
	if (answer.size() == M) {
		printV(answer);
		//sum++;
	}
	for (int i = 0; i < N; i++) {
		if (!visited[i]) {
			answer.push_back(i + 1);
			visited[i] = true;
			solution(i + 1, N, M, answer, visited);  // return solution(i+1, N, M, answer, visited); 이렇게 쓰면 안풀림 ㄷㄷ
			answer.pop_back();
			visited[i] = false;  //이게 있으면 permutation, 없으면 combination 됨 ㄷㄷ
		}
	}
	//return sum;
	return 0;
}

int main() {
	int N;
	int M;
	scanf_s("%d %d", &N, &M);

	vector<int> answer;
	vector<bool> visited(N, false);

	int sum = solution(0, N, M, answer, visited);
	//printf("%d\n", sum);
}