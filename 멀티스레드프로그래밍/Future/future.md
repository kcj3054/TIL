## 동기실행의 문제점?

- 우선 Future를 보기 전에 동기 실행의 문제점을 살펴보자... 

````
int64 Calculate()
{
    int64 sum = 0;

    for (int32 i = 0; i < 100'000; i++) sum += i;

    return sum;
}

int main()
{
	int64 sum = Calculate();
}
````
- 위의 소스는 동기 실행이다 문제점은 -> Calculate가 끝날때까지 기다려야하는 것이다. 

-  기다리면 안되나? -> main에서 다른 것들도 처리할 것이 많은데 계속해서 Calculate를 기다리게된다면 문제가 많다..  


## std::future를 사용하자

- std::future에는 비동기를 하거나 지연을 시키는 법이 존재한다.  참고로 비동기랑 멀티스레드랑 다르다 deferred는 시점을 뒤로 미루는 것이다. 뒤로미루는 것은 디자인패턴의 컴포지트 패턴이랑 비슷하다. 

- 1) deferred -> lay evaluation 지연을 해서 실행하는 것

- 2) async -> 별도의 쓰레드를 만들어서 실행

- 3) deferred | async -> 둘 중하나 실행 


## async 기법

````
future<int64> future = async(std::launch::async, Calculate);

        //TODO
        std::future_status status = future.wait_for(1ms);
        if (status == future_status::ready)
        {
            //ready 상태면 처리가 가능하다!
        }

        int64 sum = future.get(); //  결과물이 이제 필요하다! 
````

- 일반 함수말고 클래스 안의 맴버 함수에 대해서도 async가 가능한가? -> 가능하다 호출하는 방법만 다를뿐!

````
 class Knight
        {
        public:
            int64 GetHp() { return 100; }
        };
        Knight knight;
        //오른값 참조라서 &도 표시!
        std::future<int64> future2 = std::async(std::launch::async, &Knight::GetHp, knight);
````

## std::promise

- 미래에 결과물을 반환해줄꺼라 약속(promise

````
void PromiseWorker(std::promise<string>&& promise)
{
    promise.set_value("Secret Message");
}

 {
        std::promise<string> promise;
        std::future<string> future = promise.get_future();

        thread t(PromiseWorker, std::move(promise));

        string message = future.get();
        cout << message << endl;
        t.join();
    }
````

## std::packaged_task

````
void TaskWorker(std::packaged_task<int64(void)>&& task)
{
    task();
}

{
        std::packaged_task<int64(void)> task(Calculate);
        std::future<int64> future = task.get_future();

        std::thread t(TaskWorker, std::move(task));
    }
````
## 결론

- async는 자체적으로 하나의 스레드를 통해 결과물을 받는 느낌 

-  packaged_task -> 존재하는 스레드를대상으로 일감을 던지는 느낌, 결과물을 future를 받는 것 단발성, 한 번 발생하는 이벤트에 유용하다!


- 루키스님의 서버강의를 학습 후 작성하였습니다. 
