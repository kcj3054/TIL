## Redis

- Redis는 관계형 db가 아닌, NoSql이다. 빅데이터 같이 큰 데이터를 다룰 때는 필요한 기술이다. RDBS는 데이터가 크다면 그것을 모두 관계지어서 관리하기에는 힘들다..


## Redis 사용

- Redis는 기본적으로 Linux기반으로 돌아가지만 windows 위에서 포팅해서 사용할 수 있는 것이 github에 있어서 사용했습니다.

- https://github.com/tporadowski/redis/releases/tag/v5.0.9

 [##_Image|kage@qvHQD/btryt427hpd/k8KvKeQcSknHkalfC9VcS1/img.png|alignCenter|width="100%"|_##]
 
 - redis는 언어처럼 자료구조가 존재한다. 
 
 ## set, get mset mget, expire  사용
 
 [##_Image|kage@cItYe1/btryq5IaHoJ/9bskAwrKA0vhwbRbUPKkZ0/img.png|alignCenter|width="100%"|_##]
 
 
 - redis의 주요 특징 중 하나가 남아있는 수명 시간을 확인 할 수 있는 ttl [key]가 존재하고, 만료시간을 설정 할 수 있는 expire [key] [seconds]가 존재한다. 
 
 - 해당 사용법을 사용하는 예제를 생각해보자.(게임에서)
 	- 1. 로그인시 로그인이 정상적으로 되었으면 웹서버에서 확인을 하고 토큰을 발생한다. 
    - 2. 해당 토큰을 가지고 클라이언트가 gameServer로 가서 인증을 받는데 여기서 게임서버 입장에서는 이 토큰이 진짜인지 확인이 필요하다.
    - 3. 문제를 해결하기위해서는 웹서버가 클라이언트에게 토큰을 줄 때 게임서버에도 토큰을 동시에 주면되지만 이렇게 되면 시간이 지연된다.
    - 4. 여기서 중간에 Redis라는 메모리 db가 개입하게된다 redis에 토큰과 유효시간까지 넣어주면 더욱 효율적이게된다.
    

- 위의 예제에서 set kcj:auth asdfasdf    // kcj:auth라는 key에 value '토큰'은 asdfasdf이다.

- expire kcj:auth 3600 // kcj:auth키에 유효시간은 3600으로 설정  



## 정렬된 셋 (c++기준 map), 해쉬   

 [##_Image|kage@YE1j7/btryrV6YFCz/GNTU0ggFetD83dnxzpp7Ck/img.png|alignCenter|width="100%"|_##]
 
 - 정렬된 셋을 이용해서 랭킹 시스템에 적용할 수 있다 왜냐 랭킹시스템이라는 것은 정렬이 되어있어야하고, 중복이없어야하기 때문이다.
 
 ````
 zadd pvp:ranking 111 jangchae
 zadd pvp:ranking 222 kcj
 zadd pvp:ranking 14 Moon
 
 //zrange로 랭킹을 살펴본다 0 -1은 전범위를 다 보겠다는 의미
 zrange pvp:ranking 0 -1
 ````
 
 
 - 해쉬 이용법 앞에 h를 붙이면 끝~ 
 
 ````
 hset kcj:info name kcj3054 email kcj3054@naver.com
 
 hget kcj:info
 ````