## TrheadPool


- 

````c++

#include <iostream>
#include <thread>
#include <chrono>
#include <queue>
#include <functional>
#include <condition_variable>

using namespace std;

class ThreadPool
{
public:
   ThreadPool() {}
   ThreadPool(int num) 
   {
      for (size_t i = 0; i < num; ++i)
      {
         workers.emplace_back([this] {
            while (true)
            {
               std::function<void()> task;
               {
                  // mutex lock
                  std::unique_lock<std::mutex> lock(this->queuemutext);
                  
                  //condition은 람다도 가능하네?,;
                  //condition.wait에서 true라면 wait
                  // false라면 일감 실행 
                  
                  //여기서 condition.wait는 thread를 재우는 역할 
                  condition.wait(lock, [this] { return stop || !tasks.empty(); });
                  
                  //해당 부분은 thread를 재우는 것이 아니라 return 시켜버림 
                  if (stop && tasks.empty())
                     return;

                  // 태스크 큐에서 작업 가져오기
                  task = std::move(this->tasks.front());
                  this->tasks.pop();
               }

               task();
            }
            });
      }
   }

   ~ThreadPool()
   {
      {
         std::unique_lock<std::mutex> lock(queuemutext);
         stop = true;
      }
      
      condition.notify_all(); // 모든 thread 깨워서 종료 시킴 
      for (auto& worker : workers)
      {
         if (worker.joinable())
            worker.join();
      }
   }
public:

   template<typename T>
   void enqueue(T&& task)
   {
      {
         std::unique_lock<std::mutex> lock(queuemutext);
         tasks.emplace(std::forward<T>(task));
      }
      condition.notify_one();
   }

private:
   std::vector<std::thread> workers; // worker threads
   std::queue < std::function<void()>> tasks; // task queue
   std::condition_variable condition; // condition 조건 
   std::mutex queuemutext; // queue 보호용 뮤텍스 
   bool stop = false;

};

std::string getStringID()
{

}

int main()
{
   ThreadPool pool(4);

   cout << " ThreadPool Created!! " << endl;
   cout << " Enqueue Some Task! " << endl;

   for (int i = 0; i < 8; ++i)
   {
      // pool.Enqueue
   }


   return 0;
}


/*
* [mutex]
* 
* - mutual exclustion
* - 상호배타적 임
* - lock mechanism
* - 하나의 공유 변수에 여러 thread들이 접근하려고 달려드는 상황이 발생 함, 공유 resource가 존재하는 곳에.. 
* race condition이 발생하게됌 , 먼저 기회를 획득한 thread는 lock을 하고, 그 후에는 unlock을 통해 다시 다른 
* thread가 접근할 수 있다.
* 
* [semaphore]
* - signal mechanism
* - semaphore는 공유 영역에 단일 thread만 접근할 수 있는 것이 아니다. 여러 thread들이 접근할 수 있고, 
*  다른 thread들에게 접근할 수 있다는 것을 signal을 통해 알려준다 
*   예를 들어 producer consumer 생산자는 생산을 다 한후 소비자에게 '나 생산 다 했어'라고 알려줄 수 있다.
*   semaphore는 단일 공유자원이 아닌 여러 공유자원에 여러 스레드들이 접근할 수 있되, 동시에 접근할 수 있는 스레드
* 수를 조절할 수 있다. 
* 
* 
* - 두 매커니즘 모두 다르지만 semaphore가 다루기 힘들다 여러 thread드들이 동시에 접근할 수 있으니...
*/








````