## 설명 

- c++ 에서 priority_queue는 기본적으로 max 힙이다. 

- min heap으로 만들기 위해서는 비교연산자를 변경해주면되는데 해당 부분에 greater<T>를 넣어주면된다.

- 두번째 인자는 컨테이너인데 default로 vector<int>가 들어간다고 보면된다.

## 소스 
````c++
#include <iostream>
#include <queue>

using namespace std;

int main()
{
	// less<int>>
	// priority_queue<int, vector<int>, greater<int>> q;
	
	priority_queue<int, vector<int>, less<int>> q;

	q.push(1);
	q.push(3);
	q.push(5);
	q.push(2);
	q.push(7);

	while (!q.empty())
	{
		cout << q.top() << endl;
		q.pop();
	}

	return 0;
}
````