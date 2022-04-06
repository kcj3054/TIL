## cpu 파이프라인이란?

-  cpu파이프라인을 빨래방에서 빨래를 하는 것과 비슷하게 비유를 하였습니다.
	- 1. Fetch(명령어를 가지고 와라)
    - 2. Decode (명령어를 해석)
    - 3. Excute(실행)
    - 4. Write-back
    
- 이러한 cpu파이프라인에서 컴파일러는 순서를 바꿔도 결과가 같을 것같으면 최적화를 하면서 바꿀 수 있다. 말 그대로 코드 재배치 현상이 일어날 수 있다. (컴파일러가 하지않으면 cpu가 뒤바꿀 수도 있다)

- 그러나 이러한 '코드 재배치'는 멀티스레드 환경에서 문제를 일으킨다 코드 재배치 기준은 단일 스레드 기준으로 결과가 같을 경우 뒤바꾸는데 멀티스레드 환경에서 코드를 바꾸면 .. 문제가 발생한다. 

## 소스
````

#include "pch.h"
#include <iostream>

#include <thread>
#include <atomic>
#include <mutex>
#include <Windows.h>
#include <future>

using namespace std;

int32 x = 0;
int32 y = 0;
int32 r1 = 0;
int32 r2 = 0;

volatile bool ready;

void Thread_1()
{
    while (!ready)
        ;

    y = 1; // Store y
    r1 = x; //road
}
void Thread_2()
{
    while (!ready)
        ;
    x = 1; //Store x
    r2 = y; // road
}
int main()
{
    int32 count = 0;

    while (true)
    {
        ready = false;
        count++;

        x = y = r1 = r2 = 0;


        thread t1(Thread_1);
        thread t2(Thread_2);

        ready = true;

        t1.join();
        t2.join();

        if (r1 == 0 && r2 == 0) break;
    }
    cout << count << "번 수행" << endl;

}
````

- 위의 코드를 보면서 코드 재배치가 일어날때를 보자. 
````
void Thread_1()
{
    while (!ready)
        ;

    y = 1; // Store y
    r1 = x; //road
}

````
-  Thread_1()에서 코드 재배치가 일어나서 r1 = x, y = 1이 먼저 일어난다면 언젠가 if (r1 == 0 && r2 == 0) break;를 만족하면서 탈출할 때가 발생한다. 

- 루키스님의 c++서버강의를 학습 후 작성하였습니다. 