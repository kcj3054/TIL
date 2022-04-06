## TLS란?

- 쓰레드는 각기 스택영역을 자기만의 독자적인 영역을 가진다 TLS도 동일하다 각각의 독자적인 쓰레드의 영역이다.

- 문제!!! 쓰레드는 스택도 그렇고 TLS도 그렇고 모두 독자적인 공간이 왜 두개나 있나 왜 굳이 TLS가 필요한가?

	- 스택영역은 해당범위를 넘어가면 소멸하게된다 그렇지만 TLS는 진짜 자신만의 영역이다. 자신만의 전역 영역이라고 생각하면 좋을 것같다. TLS를 살펴볼 때 좋은 비유를 학습하였다. -> 뷔페에 가서 음식을 떠 오는 과정에서 조금씩 떠 오기보다. 많이 자신이 먹을 만큼 음식을 떠 오면 굳이 다시 음식이 있는 곳으로 여러번 이동하지 않아도된다.
    
- 또한 send Buffer도 TLS에 넣어 놓고 사용할 수 있다. 

    
## TLS 코드 

````

#include "pch.h"
#include <iostream>

#include <thread>
#include <atomic>
#include <mutex>
#include <Windows.h>
#include <future>

using namespace std;

thread_local int32 _LThreadId = 0;


void ThreadMain(int32 threadId)
{
    //각각의 쓰레드마다 고유한 쓰레드 ID를 가질 수 있다
    // 다른쓰레드가 다른 쓰레드의 값을 덮어쓰지않는다.

    _LThreadId = threadId;

    while (true)
    {
        cout << "I am Thread : " << _LThreadId << endl;
        this_thread::sleep_for(1s);
    }

}

int main()
{
    vector<thread> threads;

    for (int i = 0; i < 10; i++)
    {
        int32 threadId = i + 1;
        threads.push_back(thread(ThreadMain, threadId));
    }

    for (thread& t : threads)
        t.join();
}


````
[##_Image|kage@YgKsH/btryDkkQqg5/hWNynzETM0AUq3PXN7GS91/img.png|alignCenter|width="100%"|_##]


- 위의 소스에서 _LThreadId가 thread_local이 아니라면  쓰레드ID가 덮어쓰이게된다... 

- 위에서 1단계 FOR문에서 1번부터10번까지.. 돌면서 각기 쓰레드 고유한 ID를 출력한다 .. 

- 루키스님의 서버강의를 학습 후 작성하였습니다.