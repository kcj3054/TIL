## atomic??

- ATOMIC이 머야? 데이터베이스에서, ACID라는 특징이있다, A는 ATOMIC이다. 

- ?? ATOMIC? 원자적이라는 것이다. ALL OR NOTthing 모든것이 처리되거나 아니면 처리되지않거나라는 의미이다.

- 트랙젝션에서 모든 것은 원자적으로 처리되어야한다.  예를 소스로 한번보자 


## 소스
````c++
#include <bits/stdc++.h>
#include <thread>
#include <atomic>

using namespace std;

/*
Db에서 
내 계좌에서 송금을 하고 다른 계좌에서 해당 금액을 받는 것이 있다.

위의 상황이 한 트랙젝션 안에서 이루어져야하는데 그렇지 않게된다면, 문제가 생겨서 DB도 ATOMIC한 연산이 필요하다 
*/
int sum;
atomic<__int32> _sum;

void Add()
{
	for (int i = 0; i < 1'000'0000; i++)
	{
		_sum++;
		sum++;
		//_sum++는 3단계로 이루어짐
		//
	}
}

void Sub()
{
	for (int i = 0; i < 1'000'0000; i++)
	{
		_sum--;
		sum--;
		//_sum++는 3단계로 이루어짐
		/*
        int eax = sum;
        eax = eax + 1;
        sun = eax
        왜 3단계냐? cpu에서는 메모리에서 값을 가지고 와서 동시에 증가하는 연산은 하지 못한다. 
        */
	}
}
int main()
{

	Add();
	Sub();

	cout << sum << endl;

	thread t1(Add);
	thread t2(Sub);

	t1.join();
	t2.join();

	cout << sum << endl; // atomic연산 미적용
	cout << _sum << endl;  //atomic연산
	return 0;
}
````

## atomic cas 연산 

````c++

#include <iostream>
#include <thread>
#include <atomic>


using namespace std;

std::atomic<int> shared_data(0);

void increment_if_zero()
{
	int expected = 0;
	int new_value = 1;

	//cas연산을 사용해서 shared_data가 0일경우만 1로 변경 

	if (shared_data.compare_exchange_strong(expected, new_value))
	{
		std::cout << "Thread " << std::this_thread::get_id() << ": 성공적으로 값을 0에서 1로 변경했습니다.\n";
	}
	else
	{
		std::cout << "Thread " << std::this_thread::get_id() << ": 값이 이미 0이 아닙니다, 현재 값: " << shared_data.load() << "\n";

	}

}

int main()
{

	//여러 thread가 동이세 cas 연산을 시도 
	std::thread t1(increment_if_zero);
	std::thread t2(increment_if_zero);
	std::thread t3(increment_if_zero);


	t1.join();
	t2.join();
	t3.join();

	/*jthread jt1(increment_if_zero);
	jthread jt2(increment_if_zero);
	jthread jt3(increment_if_zero);*/

	cout << "최종 값" << shared_data << endl;

	return 0;
}
````