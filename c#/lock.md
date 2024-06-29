## lock

- c#에서 lock은 내부적으로 spinlock일까? context - switching 방식일까?  c#은 정말 좋은 것이 자체적으로 spinlock을 돌다가 시간이 오래 걸릴 것같으면 context - switching 방식으로 전환된다. 
- 일반적으로 대기 시간이 짧을 경우 spinlock이 더 좋고, 대기 시간이 더 길다면 context - switching 방식이 더 효율적이라서 고민을 많이 할 것이다.
    - c#은 이러한 고민들을 덜어주니 너무 좋다! 
- 내부적으로 Monitor 방식으로 작동하는데 초기에는 스핀락으로 돌다가 시간이 길어지면 컨텍스트 스위칭으로 전환한다.

- cf : c#의 Monitor는 os의 모니터방식과 동일하다. 여러 스레드가 공유 자원에 안전하게 접근할 수 있도록 도와주는 것이다. 상호 배제(임계 구역을 설정해서 자원을 사용함).. 조건 변수(condition variables.. 모니터는 스레드가 특정조건을 기다릴 수 있게 하고, 조건이 만족되면 다른 스레드가 이를 깨워주는 방식)


````c#
int counter = 0; // 공유 객체 
object lockObject = new();

var thread1 = new Thread(() => IncrementCounter(10000));
// var thread1 = new Thread(IncrementCounter);
var thread2 = new Thread(() => IncrementCounter(10000));

thread1.Start();
thread2.Start();

thread1.Join(); 
thread2.Join();

Console.WriteLine($"counter 값 : {counter}");

void IncrementCounter(int count)
{
    for(int i  = 0; i < count; i++)
    {

        //lock(lockObject)
        //{
        //    counter++;
        //}
        
        counter++;  // 값이 정확하게 나오지 않음 
    }
}
````