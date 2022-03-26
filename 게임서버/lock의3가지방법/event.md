## event.

- 

## 소스 

````

#include "pch.h"
#include <iostream>

#include <thread>
#include <atomic>
#include <mutex>
#include <Windows.h>

using namespace std;
// 한쪽에서는 클라이언트 데이터를 수신받아서 queue에 넣고, 다른쪽은 해당 정보를 추출해서 사용하는 쪽

mutex m;
queue<int32> q;
HANDLE handle;
void Producer()
{
   while (true)
   {
      {
         unique_lock<mutex> lock(m);
         q.push(100);
      }
      //signal 상태를 true로 변경해주세요 파란불로 바꿔주세요
      ::SetEvent(handle);

      this_thread::sleep_for(100ms);
   }
}

void Consumer()
{
   while (true)
   {
      //빨간불이면 잠들게 한다. !
      ::WaitForSingleObject(handle, INFINITE);

      // 가정 1. 만약 producer에서 데이터를 넣지 않는데도 불구하고 Consumer의 while이 계속햇 q의상태를 체크한다면?
      // 문제가 많다 cpu가 많이 사용된다. !  가~ 끔 producer가 데이터를 넣는다면 다른 방법을 이용해야한다 event같은기법
      unique_lock<mutex> lock(m);
      if (q.empty() == false)
      {
         int32 data = q.front(); q.pop();
         cout << data << endl;
      }
   }
}
int main()
{

   //커널오브젝트 (커널에서 관리하는 것)  
   //Usage Count 커널에서 관리하는 객체의 수 
   //Signal (파란불) / Non-Signal (빨간불)  << bool

   //2번째 메뉴얼을 true를 하면 메뉴얼을 수동으로 넣겠다는 것
   //HANDLE를 번호표라고 생각하자 여러 이벤트들 중에서 하나의 이벤트(번호표)
   HANDLE handle = ::CreateEvent(NULL/*보안속성*/, FALSE, FALSE/*InitialState*/, NULL);
   thread t1(Producer);
   thread t2(Consumer);


   t1.join();
   t2.join();

   ::CloseHandle(handle);
}
````