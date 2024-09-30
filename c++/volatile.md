## volatile 

- volatile는 C++에서 변수의 값을 컴파일러 최적화에서 제외하는 데 사용되는 키워드입니다. 즉, 컴파일러는 해당 변수가 언제든지 외부 요인에 의해 변경될 수 있다는 것을 인식하고, 그 값을 캐싱하거나 최적화하지 않습니다.


````c++
#include <iostream>
#include <thread>
#include <atomic>  // Better alternative for volatile in multithreading

volatile bool done = false;  // Without volatile, the worker might never exit the loop

void worker() {
    while (!done) {  // Compiler might optimize this loop if volatile is not used
        // Do some work...
    }
    std::cout << "Worker finished" << std::endl;
}

int main() {
    std::thread t(worker);
    std::this_thread::sleep_for(std::chrono::seconds(1));  // Simulate some work
    done = true;  // Change done to signal worker to stop
    t.join();
    return 0;
}


````


````
만약 volatile로 선언되지 않은 경우, 컴파일러는 최적화를 위해 변수를 레지스터에 캐시할 수 있습니다. 즉, 반복문 내에서 매번 메모리에서 done 값을 읽어오지 않고, 처음 읽어온 값을 캐시해 사용하게 됩니다.

이로 인해 main 함수에서 done = true로 변경하더라도, worker 함수에서 반복문은 done의 캐시된 값을 사용하여 계속해서 false인 상태로 인식하게 되어 무한 루프에 빠질 수 있습니다.

volatile은 이를 방지하기 위해 매번 메모리에서 실제 값을 읽도록 강제합니다.
````