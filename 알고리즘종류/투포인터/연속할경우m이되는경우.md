## 문제

- 주어진 숫자중에서 연속하는 숫자들을 합할 경우, 원하는 m이 되는 경우의 수를 구해야한다!

## 해결법

- 연속하는 원소들의 합을 구해야하기에 해당 연속 구간의 범위가 필요하다.

- 해당 범위내에서, 가리키는 지점이 필요하기에 투포인가 필요하다.

- 

## 소스 

````
#include <iostream>
using namespace std;


int n, m, ans;
const int maxNum = 10001;
int main()
{
	cin >> n >> m;

	int arr[maxNum] = { 0, };

	for (int i = 1; i <= n; i++) cin >> arr[i];


	int sum = arr[1];
	int j = 1;
	for (int i = 1; i <= n; i++)
	{
		while (j <= n)
		{
			if (sum == m)
			{
				ans++;
				sum -= arr[i];
				break;
			}
			else if (sum < m)
			{
				j++;
				sum += arr[j];
			}
			else if (sum > m)
			{
				sum -= arr[i];
				break;
			}
		}
	}

	cout << ans;
	return 0;
}
````