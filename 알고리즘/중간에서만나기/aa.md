#include <bits/stdc++.h>

using namespace std;

int n, s, m;
int main()
{
	cin >> n >> s;
	
	vector<int> a(n);
	for (auto& i : a) cin >> i;
	
	m = n / 2;
	n = n - m;
	// 총길이 n을 반쪽인 n으로 말하기 
	// n과 m으로 둔다  각각을 모든 부분 집합의 합으로 놓기 


	vector<int> first(1 << n);

	for (int i = 0; i < (1 << n); i++)
	{
		for (int k = 0; k < n; ++k)
		{
			//i에 대해서 k번째 비트가 1로된 경우 
			if(i & (1 << k)) first[i] += a[k];
		}
	}
	vector<int> second(1 << m);

	for (int i = 0; i < (1 << m); i++)
	{
		for (int k = 0; k < m; ++k)
		{
			if(i & (1 << k)) second[i] += a[k + n];
		}
	}

	sort(first.begin(), first.end());
	sort(second.begin(), second.end());
	reverse(second.begin(), second.end());
	//sort(second.rbegin(), second.rend());  // second도 첫번째부터 보기 위해서 reverse 

	n = (1 << n);
	m = (1 << m);

	int i = 0, j = 0;
	long long ans = 0;

	while (i < n && j < m)
	{
		if (first[i] + second[j] == s) {
			long long c1 = 1;
			long long c2 = 1;
			j += 1;
			i += 1;

			while (i < n && first[i] == first[i-1])
			{
				c1 += 1;
				i += 1;
			}
			while (j < m && second[j] == second[j - 1])
			{
				c2 += 1;
				j += 1;
			}
			ans += c1 * c2;
		}
		else if (first[i] + second[j] < s) { // first가 오름차순, second가 내림 차순 
			i += 1;
		}
		else j += 1;
	}

	
	if (s == 0) ans--; //공집합인 경우 
	cout << ans;
	return 0;
}