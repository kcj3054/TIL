## CountingArray

- CountingArray란? 투포인터 사용 중 일종의 트릭이라고 생각하면된다.

- 해당 구간에서 숫자의 갯수를 보관하는 배열을 CountingArray라고 보자!



## 예시 

- 투포인터의 범위 i ~ j 일때 j가 증가해서 j + 1이 되기전에 CountingArray를 통해 j + 1의 값이 원하는 갯수를 초과한다면  j + 1를 무시하면된다.



## 예시 문제!

- n개의 숫자가 있을 때 중복되는 수가 있으면 안될 때, 가장 큰 구간의 크기를 구하라!

````
#include <iostream>
using namespace std;

#define MAX 100001
int main()
{
    int n = 0; cin >> n;
    int ans = 0;
    int arr[MAX] = {0, };
    int countingArray[MAX] = {0, };

    for(int i  = 1; i <= n; i++) cin >> arr[i];

    int j = 1;
    countingArray[arr[1]]++;

    for(int i = 1; i <= n; i++)
    {
        while(j + 1 <= n && countingArray[arr[j + 1]] == 0)
        {
            countingArray[arr[j + 1]]++;
            j++;
        }

        countingArray[arr[i]]--;
        ans = max(ans, j - i + 1);
    }

    cout << ans;
    return 0;
}
````