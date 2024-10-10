## condition_variable

````c++
#include <condition_variable>
#include <mutex>
#include <thread>

std::queue<int> dataQueue;
std::mutex mtx;
std::condition_variable cv;
bool done = false;


void producer(int dataCount)
{
	for (int i = 1; i <= dataCount; ++i)
	{
		std::unique_lock<std::mutex> lock(mtx);
		dataQueue.push(i);
		std::cout << "Produced : " << i << std::endl;
		lock.unlock();

		//data를 생성했으니 대기 중인 소비자 스레드에게 알린다. 
		cv.notify_one();

		std::this_thread::sleep_for(std::chrono::milliseconds(100));
	}

	// 모든 데이터 생산이 완료됨
	std::unique_lock<std::mutex> lock(mtx);
	done = true;
	lock.unlock();
	cv.notify_all();  // 모든 대기 중인 소비자에게 알림
}

void consumer()
{
	while (true)
	{
		std::unique_lock<std::mutex> lock(mtx);

		/*
		*  - cv가 mutex가 잠기지 않은 상태에서 호출하면 ub가 발생한다. 
		*  - 조건이 만족될 때까지 스레드를 일시 중단
		*  -  이 때 mutex를 자동으로 해제하여 다른 스레드가 자원을 사용할 수 있게 합니다.
		* - 조건이 만족되면, 다시 mutex를 잠가서 안전하게 자원에 접근할 수 있도록 합니다.
		*/

		/*
		*  cv.wait()는 mutex가 잠긴 상태에서 호출됩니다. 
		wait()는 내부적으로 mutex를 잠시 해제하여 다른 스레드가 자원을 사용할 수 있게 한 뒤, 
		조건이 충족되면 다시 mutex를 잠가서 안전하게 작업을 진행합니다.
		*/

		//두번째 인자로 조건을 확인하는 람다 함수 
		//조건이 true일 경우 thread는 깨어난다 
		cv.wait(lock, [] {return !dataQueue.empty() || done;  });

		if (dataQueue.empty() == false)
		{
			int data = dataQueue.front();
			dataQueue.pop();
			std::cout << "consumed : " << data << std::endl;
		}
		else if (done)
		{
			//처리할 데이터가 없다 
			break; 
		}
	}
}


int main()
{
	std::thread prodThread(producer, 10);  // 10개의 데이터를 생산하는 스레드
	std::thread prodThread2(producer, 20);  // 10개의 데이터를 생산하는 스레드
	std::thread consThread(consumer);      // 데이터를 소비하는 스레드

	prodThread.join();

	consThread.join();

	return 0;

}
````


## 여러 생산자와 단일 소비자일 경우 

````c++

#include <iostream>
#include <thread>
#include <mutex>
#include <condition_variable>
#include <queue>
#include <atomic>

std::queue<int> dataQueue;
std::mutex mtx;
std::condition_variable cv;
std::atomic<int> producerCount(0);  // 생산자가 몇 개 남았는지 추적
bool done = false;

void producer(int id, int dataCount) {
    for (int i = 0; i < dataCount; ++i) {
        std::unique_lock<std::mutex> lock(mtx);
        dataQueue.push(i + id * 100);  // 생산자 ID를 기반으로 다른 값을 생성
        std::cout << "Producer " << id << " produced: " << (i + id * 100) << std::endl;
        lock.unlock();
        cv.notify_one();  // 대기 중인 소비자에게 데이터가 준비되었음을 알림
        std::this_thread::sleep_for(std::chrono::milliseconds(100));  // 임의의 지연
    }

    // 생산 작업이 완료되면 카운트를 줄인다.
    producerCount--;
    if (producerCount == 0) {  // 모든 생산자가 작업을 끝냈다면
        std::unique_lock<std::mutex> lock(mtx);
        done = true;
        lock.unlock();
        cv.notify_all();  // 모든 소비자에게 알림
    }
}

void consumer() {
    while (true) {
        std::unique_lock<std::mutex> lock(mtx);
        cv.wait(lock, [] { return !dataQueue.empty() || done; });  // 데이터가 있거나 생산이 끝났는지 대기
        if (!dataQueue.empty()) {
            int data = dataQueue.front();
            dataQueue.pop();
            std::cout << "Consumed: " << data << std::endl;
        } else if (done) {
            break;  // 생산이 끝났고 더 이상 처리할 데이터가 없음
        }
    }
}

int main() {
    const int numProducers = 3;  // 3개의 생산자 스레드
    const int numItems = 5;      // 각 생산자당 5개의 아이템을 생산

    producerCount = numProducers;  // 생산자 카운트 초기화

    std::thread producers[numProducers];
    for (int i = 0; i < numProducers; ++i) {
        producers[i] = std::thread(producer, i, numItems);
    }

    std::thread consThread(consumer);  // 데이터를 소비하는 스레드

    for (int i = 0; i < numProducers; ++i) {
        producers[i].join();  // 모든 생산자 스레드가 끝날 때까지 기다림
    }

    consThread.join();  // 소비자 스레드가 끝날 때까지 기다림

    return 0;
}


````