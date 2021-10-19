## cpu 스케쥴링이란 ?

1. cpu 효율을 높이기 위해서 cpu에게 항상 실행중인 프로세스를 가지게 하는 것이다.

2. 어떤 프로세스가 대기해야 할 경우 운영체제는 cpu를 그 프로세스로부터 회수해 다른 프로세스에 할당한다.



### 선점 스케쥴링 

1. 프로세스가 실행 상태에서 준비완료 상태로 전환될 때 

2. 프로세스가 대기상태에서 준비완료 상태가 될때 

선점이란 -> 다른 상태를 빼앗은 것이라고 생각하자

### 비선점 스케쥴링

비선점 스케쥴링은 앞에 있는 프로세스가 다 끝날때까지 기다렸다가 내 차례가 오면 시작하는 것이다. 

### 디스패처 (Dispatcher)

디스패처는 cpu의 제어를 단기 스케줄러가 선택한 프로세스에게 주는 모듈이다. 

다시 말해서 일정을 정하는 것은 스케쥴러고 그것을 행하는 것은 디스패처가 행한다.


### 스케쥴링 기준 

어떻게 해서 스케쥴링을 할 것인가에 대해 생각해보자!

* cpu 이용률

* 처리랑

* 총처리 시간

* 대기시간 

* 응답시간

## 스케쥴링 알고리즘 

#### 선입선출 알고리즘(FCFS)


#### 최단작업 우선 스케쥴링(SJF) 

가장 작업량이 짧은 것을 오게하면 waiting 시간이 당연하게 짧아진다.

이론적으로는 이상적이다. 

문제점- > 어느 cpu가 가장 짧은것인지 확인하지 못한다 예측만 할 수있다 .




# ============================================================================

#### 더 추가적으로 공부 

### cpu-burst time분포

- io bound job, cpu bound job이 있는데 io를 많이 하면 io바운드 잡, cpu 사용하는 시간이 길면 cpu bound job이다. 이때 두가지가 있을 경우 어느 경우에 cpu를 먼저 주는 것이 유리할까? 정답은 IO bound job이다 왜냐? i/o bound job에 주고 나서 cpu를 조금만 쓰고 다시 그 cpu를 cpu bound job에게 주면 두개 다 사용 가능한 반면, cpu bound job에 먼저 cpu 우선권을 주게되면 cpu를 너무 길게 사용해서 io작업을 못할 수도있다

[##_Image|kage@G4WWw/btrigIV8fOL/gNwtv9A6C2mFKg1Jl54X5k/img.png|alignCenter|width="100%"|_##]



### cpu scheduler & dispatcher

- cpu scheduler는  ready 상태의 프로세스 중에서 cpu를 줄 프로세서를 '선택'하는 작업을 한다

- Dispatcher
	- 디스패처는 cpu 스케쥴러가 선택한 프로세스에게 cpu제어권을 넘기는 '행위'를 하는 것이다.
    
    
- cpu 스케쥴링이 필요한 경우

	- 1.running -> blocked ( io 요청하는 시스템콜)\
    - 2. running -> ready (timer가 다 된경우)
    - 3. blocked -> ready (io 완료 후 인터럽트)
    - 4. 작업 완료 후 종료
    
* 1 4는 nonpreemptive이지만 2, 3은 강제로 cpu를 빼앗겨서 preemtive이다.



### 스케쥴링을 결정하는 요인

- cpu 이용율 (cpu에게 얼마나 많이, 오랫동안 일을 시키는지 확인)

- 처리량 ( 산출물)
- 대기시간 (cpu를 얻고 ready queue까지 가는데 걸린 총 시간이댜)

- 응답시간 ( 응답시간은 cpu를 최초로 얻기까지 걸린시간이다

-> 응답시간과 대기시간은 차이가 있다 왜냐하면 처음으로 cpu를 얻었다고는 하지만 그 후에 인스트럭션이 걸려서 다시 cpu제어권이 다른 곳으로 넘어 갈 수도있기 때문에  cpu를 얻자마자 바로 ready queue로 들어갈 수 있는 것은 아니다. 



# cpu 스케쥴링 종류 


##  FCFS( First -Come First - Served)

* 말그대로 먼저 오면 먼저 받는 것이다 그러나 여기서 시간이 오래 걸리는 것이 먼저 와서 먼저 cpu를 할당 받게 되면 평균적으로 wait시간이 길어진다 이것을 convoy effect라고하는데 다른분들 중에서 똥차효과라고 부르시는분들도 있었습니다

[##_Image|kage@1HxbF/btrijreNOKB/UExNHl1FifHYWDnhbnQMlK/img.png|alignCenter|width="100%"|_##]

위 사진처럼 p1이 오래걸리는데 먼저 받아버리면 평균 wait가 길어지지만 p2나 p3를 먼저 받으면 평균 웨이트가 짧아진다


## SJF( Shortest - job - first)

- cpu burst time이 가장 짧은 프로세스를 제일 먼저 스케쥴 하는 것이다 

- 여기서는 nonpreemptive 방식과 preemptive방식이 있지만 preemptive방시기 전형적인 sjf라고 할 수 있다 sjf는 최적의 평균 waiting time을 보장한다 하지만 여기서는 몇가지 문제점이 있다 

- 문제점 
	-  nonpreemptive 방식은 선점이 없기에 문제가 없지만 preemptive 방식은 선점이 있는데 다시 새로 채워진 것들 중에서 더 시간이 짧은 것들이 생기면서 순서가 자꾸 변하면 결국에는 기아현상이 발생한다 (cpu 할당을 받지 못하는 프로세스가 발생할 수 있다)

	-  또 다른 문제점은 어떤 프로세스가 sjf인지를 알 수 없기에 예측만 할 수 있다는점이다 예측할때는 최근 job에 가중치를 더 줘서 계산을 하지만 어디까지나 예측이다
    
[##_Image|kage@biTcew/btrijrsi9IE/aYvHeK98KiBOg6uMF3nwW1/img.png|alignCenter|width="100%"|_##]


## priority scheduling

- 이것도 sjf랑 비슷하다 여기서 말하는 우선순위랑 sjf에서 말하는 짧은 일이랑 동일한 의미로 볼 수 있다

- 그럼 여기서도 sjf에서 발생하는 starvation현상이 발생한다 이러한 것들을 해결하는 방법은 aging을 시키는 것이다 

- 해결법 -> aging을 시켜서 시간이 흐를 수록 오래 있었던 프로세스에게 우선순위를 높여주는 방식이다



## Round Robin(RR)

- 각 프로세스는 동일한 크기의 할당 시간 (time quantum)을 가지게된다 이것을 timer느낌을 보면된다 

- 할당 시간이 지나면 선점당해서 ready queue로 들어가게된다 

- 라운드로빈 방식이 좋은점은 일반적으로 sjf보다 response time이 더짧다

- 본인이 cpu 사용할 시간에 비례해서 순서를 기다리기에 비교적 합리적이다. 왜냐?
	- 할당시간이 정해져있는데 cpu를 짧은 시간내에서 처리하고 떠날 수 있는 것은 그렇게 해서 떠나면 되고 만약 긴 시간동안 cpu를 점유해야하는 프로세스들은 할당시간동안 사용한 후 다시 ready queue로 들어가서 대기한 뒤 다시 cpu를 할당 받아서 처리하는 동작을 반복하게 되니.. 긴 시간을 필요로하는 것은 길게 기다리고 짧은 시간을 필요로하는 것은 짧게 하고 빠지면 되는 것이다.
    


## Mutilevel Queue

- ready queue를 여러개로 분할 하는 것이다(foreground랑 background로 분리하는 것이다)

- 포그라운드랑 백그라운드 각각은 독립적인 스케쥴링 알고리즘을 가진다 그래서 각 큐에 대한 스케쥴링이 필요하다 


#### Fixed priority scheduling 
- Fixed priority scheduling은 모든 포그라운드 작업을 다 한후에 백그라운드 작업을 하는 것이다 이때 포그라운드 작업을 계속해서 끝내지 못한다면 백은 작업을 하지 못하기에 starvation현상이 발생 할 수 있다 


#### Time slice 

- 각 큐에 cpu time을 적절한 비율로 할당하는 것이다 



## Multilevel Feedback Queue

- 프로세스가 다른 큐로 이동이 가능한 것이다

-  멀티레벨 피드벡 큐 scheduler를 정의하는 파라미터들
	- 큐의 수 
    - 각 큐의 scheduling algorithm
    - process를 상위 큐로 보내는 기준
    - proecss를 하위 큐로 내쫓는 기준
   	- .. 


- 밑의 사진은 멀티레벨 피드벡 큐를 구현한 예이다

- 멀티레벨큐와 차이점은 멀티레벨큐는 starvation이 발생 할 수 있지만(위쪽의 큐가 비지 않으면 아래쪽을 실행하지 않으니 ) 멀티레벨 피드벡큐는 aging을 적용하기에 starvation을 발생하는 것을 줄일 수 있다

[##_Image|kage@cEMecJ/btricEUHDTd/BJ0cBEjbkANmg9Mu95ucjK/img.png|alignCenter|width="100%"|_##]



## Multiple - Processor Scheduling



## Real - Time Scheduling

- Hard real-time systems
	-  반드시 데드라인안에 프로세스를 끝내도록 하는 것이다. 
    
- Soft real-time computing
	- 일반 프로세스랑 섞으면서 , 일반 프로세스에 비해 높은 우선순위를 가지도록  한다 
    - 예를들면 동영상은 초당 24프레임이 발생한다 그러나 이것을 지키지 못한다면 사용자 불편은 하겠지만 더 큰일은 발생하지 않는다 이러기에 소프트 리얼 타임으로 볼 수 있다
    


출처 : https://sbell92.tistory.com/25
		반효경 교수님 운영체제 강좌
        공룡책 