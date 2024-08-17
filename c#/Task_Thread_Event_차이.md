# c# Thread, Event, Task 차이 

- Event, Task 모두 비동기를 위함 c# 기법입니다. 

- Task는 기본적으로 스레드풀을 사용하며, 작업을 예약하고 관리한다. 
    - Task는 async await와 함께 사용할 수 있다. , -> c# db쪽 작업을 처리할 때 async Task FunctionName() ~  await sp 호출.. 이렇게 사용했었다. 
    - c# async await가 Task기반 프로그램이다. -> 일감이 한 120개가 존재하고 스레드가 3개가 존재한다고 가정할 대 40개씩 Task라는 논리로 묶어서 각 스레드에게 할당 함
- Event는 특정 작업이 발생했을 때 실행할 코드를 등록하고, 그 작업이 발생하면 등록된 코드를 호출하는 매커니즘. 

-  Task도 Thread이다. -> 하지만 Task는 .net 스레드풀을 사용한다. 작업이있다면 작업을 적절이 스케쥴링하여 분배된다.   
   -  Task는 구현하는 작업 그 자체를 의미, Thread는 작업을 수 많은 작업자들 중 하나를 의미한다.

- c#의 Parallel클래스 for, foreach()등의 메소드를 제공하여 병렬처리를 쉽게 도와줌. 
    - 더미 클라이언트 제작시 효율을 생각하여 일감을 처리할 때 Parallel을 사용한 부분이 있었다 -> 하지만 시니어분들의 조언에서는 Parallel도 Thread를 여러개 사용하는 것이고, 스레드 또한 비용이다 굳이 해당 부분에서 Parallel을 사용할 필요가 없다고 조언을 받음 

- async void 를 사용하면 테스크가 await가 안된다. -> 
  - ->async Task는 비동기 작업이 완료될 때까지 기다릴 수 있다, 그렇지만 async void를 사용하게된다면 await로 기다리지 않으니, 결과를 호출자가 알 수가 없고, 호출 후 바로 결과가 반환되므로 비동기 작업 결과를 추적하거나 후속처리를 할 수 없다. 
  - > async Task는 발생한 예외들을 Task 객체에 담을 수 있다. 그렇지만 async void는 그러한 것이 불가능해 try - catch도 안되고 예기치 않은 종료가 발생할 수 있다. 
  - > event handler일 경우 async void가 가능하다.
    - > 이유는 .. 
  - https://www.sysnet.pe.kr/2/0/11414
  


  