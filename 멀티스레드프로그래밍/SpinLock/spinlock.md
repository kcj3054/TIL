## SpinLock

- SpinLockd은 lock이 있을 경우 자기 자리로 다시 돌아가는 것이 아닌 주위에서 계속해서 빙글빙글 돌아다닌 것을 의미한다.



## spinlock 소스

````

#include "pch.h"
#include <iostream>

#include <thread>
#include <atomic>
#include <mutex>
using namespace std;

class SpinLock
{
public:
    void lock()
    {

        //CAS(Compare-And-Swap)

        bool expected = false; // 락을 걸기를 원하는 대상의 현재상태 그러나 현재는 false이다
        bool desired = true;  // 락이 걸리기를 기대하는 것

        ////CAS 의사코드 
        //if (expected == _locked)
        //{
        //   expected = _locked; // ???
        //   _locked = desired;  // 현재 lock을 true로 변경 
        //   return true;
        //}
        ////다른 누군가가 lock을 선점한 상태 !
        //else
        //{
        //   expected = _locked;
        //   return false;
        //}
        while (_locked.compare_exchange_strong(expected, desired) == false)
        {
            //expected가 &로 받아와서 항상 expected = false로 줘야한다
            expected = false;
        }
    }
    void unlock()
    {

    }
private:
    atomic<bool> _locked = false;
};

int32 sum = 0;
mutex m;

void Add()
{
    for (int i = 0; i < 1'000'000; i++)
    {
        lock_guard<mutex> guard(m);
        sum++;
    }
}
void Sub()
{
    for (int i = 0; i < 1'000'000; i++)
    {
        lock_guard<mutex> guard(m);
        sum--;
    }
}
int main()
{
    volatile int32 a = 1;
    a = 2;
    a = 3;
    a = 4;

    thread t1(Add);
    thread t2(Sub);

    cout << sum;
}
````

- 멀티스레드 환경에서는 공유 영역에있는 sum을 접근할때는 lock을 걸어 놓고 사용을 해야한다 그래서 Add, Sub에서 연산을 하기전에 lock을 걸어놓는다 

````
//다른 누군가가 lock을 먼저 걸었다면 while안에서 뱅글뱅글 돈다. 
 while (_locked.compare_exchange_strong(expected, desired) == false)
        {
            //expected가 &로 받아와서 항상 expected = false로 줘야한다
            expected = false;
        }
````

- 위의 atomic에는 compare_exchange_strong이 존재한다 앞에는 예상한 값, 뒤에는 기댓값이다  위의 소스에서  _locked.compare_exchange_strong(expected, desired) == falsed라면  계속해서 빙글빙글 while을 도는 것이 spinlock이다. 현재 다른 누군가가 lock을 선점한 상태라는 의미이다. 

- 락을 걸기 위해서 expected = false로 해 놓는 것은 해당 값이 락을 걸고 싶은거지 현재 lock이 걸려있는 것은 아니다 그래서 false.

- 그리고 우리가 희망한 것은 lock이 걸리기릴 희망한 것라서 기댓값은 desired = true로 해놓는다. 

## spinLock 좋은건가? 나쁜건가?

- spinLock은 양날의 검이다 왜? 
	- spinLock이 길어지면 cpu 점유율이 높아진다(단점)
    - 그러나 금방 해제 될 lock이라면 제자리로 돌아갔다오면 context Switch가 발생해서 거기에 해당하는 비용이 더 들어가기에 대기하고 있다가 들어가는 것이 더 효율적이다. 
    
    
- 루키스님의 서버 강의를 학습 후 작성하였습니다. 