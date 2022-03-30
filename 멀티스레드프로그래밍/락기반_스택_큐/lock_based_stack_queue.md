## 락기반의 스택, 큐

- 일반적인 스택 큐를 사용할때랑 멀티스레드 프로그래밍에서 스택 큐를 사용때는 조금 다르다..

- empty체크에서 1개가 남아있을 경우 비어있지 않다고 말해줄 수 있을텐데 만약 그순간에 다른 스레드가 pop을 하면 이것은 비어있는 현상이 된다.. 


## main 소스

````

#include "pch.h"
#include <iostream>

#include <thread>
#include <atomic>
#include <mutex>
#include <Windows.h>
#include <future>

#include "ConcurrentQueue.h"
#include "ConcurrentStack.h"

LockQueue<int32> q;
LockStack<int32> s;
using namespace std;

void Push()
{
	while (true)
	{
		int32 value = rand() % 100;
		q.PUsh(value);

		this_thread::sleep_for(1ms);
	}
}

void Pop()
{
	while (true)
	{
		int32 data = 0;
		if (q.TryPop(data)) cout << data << endl;
	}
}

int main()
{
	thread t1(Push);
	thread t2(Pop);

	t1.join();
	t2.join();

}
````