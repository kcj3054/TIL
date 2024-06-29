- 소켓프로그래밍이 tcp udp부터 시작해서 select wsaEvent, overlapped, .. 까지해서 IOCP가 나오기까지를 확인해보자.

- 각 모델 별로 장단점을 정리하면서 IOCP의 특정도 적어 놓겠습니다.

````

------------------- select 모델  (안드로이드에서 하면 문제가 없다, 안드로이드는 linux플랫폼기반이니)
	-장점 : 윈도우 리눅스 공통
	-단점 : 성능이 안좋다 왜냐? 소켓set에 계속해서 등록을 해줘야하기에, 갯수 제한 64개
 ----------------------------wsaEventSelect 모델-------------------------------------------
	- 비교적 뛰어난 성능이지만 64개 갯수제한이 동일하게 있다
------------------------------------------------- Overlapped (이벤트 기반)------------------------
	- 장점은 성능이 좋다 단점은 64개로 갯수제한
 ------------------------------Overlapped (콜백 기반)------------------------------------------
	1.성능이 좋지만 단점은 모든 비동기 소켓 함수에서 사용가지않다 (accept에는 callback을 걸 수가없다)
   	2. 빈번한 alertable wait로 인한 성능이 저하된다.
    3. apc큐자체가 쓰레드별로 각자있다. 다른 쓰레드가 대신 처리를 못한다는 단점이 있따.


````

- Reactor Pattern (논블로킹 소켓인데 소캣 상태를 확인후 뒤늦게 RECV, SEND를 호출한다)

- Proactor Pattern (미리 RECV나 SEND를 하고, overlapped WSA로 미리 걸어 놓은 후 내부적으로 처리하도록한다



### IOCP (Completion Port) 모델

- Overlapped 콜백 방식에 있었던 APC개념을  Completion Port로 대체했는데 쓰레드마다 있는건 아니고 1개만 있다 중앙에서 관리하는 큐느낌이다

-  Completion Port처리를 GetQueueCompletionStatus

- iocp의 port는 socket에서의 port와 느낌이다르다 socket port는 bind 시 port를 
엮는 것인데 iocp의 port(completion port)는 포트랑 스레드를 묶는 것이다. 
- 워커 스레들 중 하나가 cp에서 입출력 완료를 꺼냄 

- IO(RECV, SEND) 작업에서 동시 수행되는 스레드 개수의 상한선을 설정하여 CPU를 효율적으로 사용하자

![](../../iocp_생성.PNG)

- CreateIoCompletionPort는 두번 사용되는데 iocp 핸들을 생성할 때 그리고 socket을 cp에 등록할 때 2번째인자인 ExistingCompletionPort에 null이면 iocp 핸들 생성이라고 생각하면 됌  

-GetQueuedCompletionStatus에서 TimeOut 에러는 괜찮음
	- Timeout 에러는 단순히 함수가 호출된 시점에서 처리할 완료된 I/O 작업이 없다는 것을 나타내며, 이는 비동기 I/O 작업이 아직 완료되지 않았거나, 아직 처리해야 할 작업이 없다는 것을 의미합니다.

- https://www.slideshare.net/namhyeonuk90/iocp