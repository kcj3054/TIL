#### 데이터 연산

-   데이터를 연산할때는 cpu에서 연산을 한다, 첫번째로 저장공간인 메모리에서 데이터를 연산할 데이터를 가지고 와서 (2)cpu에서 연산을 처리하고 (3)연산 결과를 다시 메모리에 넣는다

[##_Image|kage@bbvuUa/btriizZSEOC/guFtdxN48BK9kaV8HSt4Jk/img.png|alignCenter|width="100%" data-origin-width="836" data-origin-height="600" data-ke-mobilestyle="widthOrigin"|||_##]

### Race Condition

-   공유하는 데이터가 있을 경우 서로 다른 프로세스가 공유데이터에 접근할 하면서 연산을 수행할 경우 문제가 발생한다
    -   예를 들어서 (1)++연산자가 연산을 할려고 접근을 했다가 (2)중간에 시스템콜이 걸려서 수행을 온전히 다 하지 못하는 상태에서 (3) - - 연산 프로그램이 들어와서 --연산을 완료한 후 (4) 다시 1번 연산을 작동하면 ++ 연산이 제대로 이루어져있지않는다 이럴때 문제가 발생한다
-   그런데 왜? 이런 문제가 발생하는가? (cpu가 여러개일때는 발생하고, cpu가 하나일때도 문제가 발생할 수도 있다 )
    -   프로세스는 독립적인 메모리공간을 가지고 있어서 문제가 발생하지 않는 것아닌가?
    -   이유는!!!! os가 관여하기때문이다 프로세스들은 본인들이 하지 못하는 일을 os에게 부탁하는데 이때 시스템 콜을 한다 그러한 상황에서 a도 시스템 콜한 상황에서 cpu할당 시간이 끝나서 b에게로 넘어간 상태에서 b도 시스템 콜한 상황에서 a의 요청에서 건드리던 데이터를 b의 요청의 공간도 os가 건드리면 문제가 발생한다...
    -   간단히 다시말하자면 프로세스가 커널을 건드리는 도중에 cpu제어권이 다른 곳으로 넘어가서 넘어간 곳에서도 이전 프로세스가 건드리던 곳을 os에게 부탁해서 작업을 하게된다면 문제가 발생한다..

[##_Image|kage@cuNBSv/btrikLsBtzF/q6T1uQsMx9ZuHkawFxBjVK/img.png|alignCenter|width="100%" data-origin-width="816" data-origin-height="580" data-ke-mobilestyle="widthOrigin"|||_##]

### os에서 race condigion 발생시기

-   kernel 수행 중 인터럽트 발생 시
-   process가 system call을 하여 kernel mode로 수행 중인데 context switch가 일어나는 경우
-   multiprocessor에서 shared memory내의 kernel data

밑의 그림에서는 커널모드에서 수행 중일때 context switch가 일어나는 경우이다...

[##_Image|kage@rXREt/btrinslxXlD/Nc3UasTSBVrZL1EFSFcCq0/img.png|alignCenter|width="100%" data-origin-width="761" data-origin-height="581" data-ke-mobilestyle="widthOrigin"|||_##]

### multiprocess에서 race condition 발생

커널모드 중간에 발생할때는 cpu수행시 인터럽트를 안걸면 방지 할 수 있다고 했는데 그렇지 않다 이유는 cpu가 여러개이면 한쪽의 인터럽트를 막았다고 해도 다른 cpu가 해당 자원에 접근하여 일을 할 수 있기때문이다...

-   해결법 -> cpu하나만 커널모드를 들어가게하면된다... 엥?
    -   안된다! 왜냐? cpu가 여러개인데 그 중에서 하나만 커널모드를 들어가게 한다면 나머지 cpu는 놀고있기때문에 그러면 오버헤드가 너무 크다..
    -   그래서 동시에 접근할려는 그 자원에 대해서만 lock을 걸면된다..

### cf

```
- 데이터를 읽어와서 연산 하는 과정을 atomic하게 이루어지면 문제가 발생하지 않는다.
- 프로세스끼리는 자신만의 독립된 메모리 영역을 가지기에 공유데이터문제가 발생하지 않는다 그러나 발생 이유는 os관여로..
```

### critical section

-   크리티컬 섹션은 잘못 알고 있었던 부분이 있었다 평소에 크리티컬 섹션은 공유데이터 공간을 크리티컬 섹션이라고 알고 있었는데 그렇지 않다 공유데이터에 접근 하는 양 프로세스의 코드가 크리티컬 섹션이다....

[##_Image|kage@68iAN/btriiAYNyBe/XrEdLpyGe1knsZGfjpRs4k/img.png|alignCenter|width="100%" data-origin-width="812" data-origin-height="593" data-ke-mobilestyle="widthOrigin"|||_##]

## critical section 해결법

-   상호배제 (mutual exclution)
    -   크리티컬 섹션 영역에는 한번에 하나의 프로세스만 들어갈 수 있도록 하는 것이다. .
-   progress
-   bounded waiting(유한대기)
    -   프로세스 a, b, c가 있을 경우 a가 들어가고 나왔다고 b가 들어가고 나왔다가 다시 a가 들어갔다가 나오고 a b두개의 process가 반복을 하면 남아있는 c도 분명 들어가고싶은데 들어갈 수가 없다 이러한 문제를 해결하기 위해서 유한대기를 줘서 기다리는 것도 무한정 기다리는 것이 아니라 유한하게 기다리도록 하는 것이다...

-   해결 알고리즘
    -   피터슨 알고리즘
        -   깃발을 통해서 자신이 들어 가고싶다고 표시하고 , 상대방의 의견도 확인한다.
        -   그리고 자신의 턴도 있고 상대방의턴도 있고 자신의 턴에서 자신이 깃발을 들고 있으면 들어갈 수 있다....

```
    - 자신의 턴일때 턴을 수행중에 먼저 턴을 상대방으로 돌려 주고 (turn = j) 난후 while 조건을 보면서 턴이 상대방이고 상대방이 깃발을 들었을때만 기다리고 아니면 크리티컬 섹션에 들어가서 일을 한 후 자신의 깃발도 false로 내려준다

    - 이 피터슨 알고리즘이 좋은 이유는 다른 알고리즘들은 자신의 턴에해당할때 크리티컬 섹션에 들어가고싶지 않더라도 들어가야해서 낭비였는데 여기서는  들어가고싶고!!!!! && 자신의턴!!! 일때만 수행해서 더 효율적이다... 


- 문제점이 있다... !!!

- busy waiting문제가 발생한다 spin - lock이라고도 불린다 이유는???

- while 조건을 보면서 자신의 차례가 아니면 while문 주위를 빙글빙글 돌기때문이다....  
```

[##_Image|kage@oiJ7J/btrion5aOfr/TF4ikZVIaZCZzm9Nv1Fnmk/img.png|alignCenter|width="100%" data-origin-width="751" data-origin-height="540" data-ke-mobilestyle="widthOrigin"|||_##]