## windows redis 사용 

- windows에서는 redis를 사용하기위해서 windows redis를 사용하거나, ubuntu를 설치해서 redis를 사용하는 것도 존재한다.

- windows에서 ubuntu를 사용?
    - wsl(windows subsystem linux)를 이용하면 ubuntu를 사용할 수 있다.

    - 설치 방법 
        - windows 기능 켜기 끄기 에서 가상 머신을 on한다
        - cmd에서 wsl2로 설정한다. 
        - windowsAppStore에서 ubuntu를 설치 후 재시작하면 해당 화면을 볼 수 있다. 
        
        ![](./ubuntu초기회면(windows).png)

- ubuntu에서 바로 redis를 설치해도 좋지만 docker위에서 사용한다면 더욱 편리하게 사용가능하다, docker에 대해서는 더욱 알아보는 것으로하자.


### ubuntu에서 docker 설치 

- sudo su (super user로 권한 전환 )
- sudo apt update && apt install redis-server (설치)
- systemctl status redis-server (redis-server 상태확인)
    - systemctl(control)로 service의 상태, 재시작, 중지, 시작 가능 
    

### redis test

- redis-server가 실행 중일 때 테스트를 할 때 redis-client를 사용해보면된다. 
    - cli 화면에서 redis-cli

- http://redisgate.kr/redis/configuration/redis_start.php
    - 해당 주소에서 기본 명령어들을 학습  

- 


## c#에서 redis 사용 

- cloudstructure를 사용한 것이 stackexchange를 간단하게 사용하기 위해서 랩핑한것. ! 

- c# gameserver에서 redis를 사용할 때 주로 tocken을 넣고 삭제하기도한다 (login 시 애용)


````
using CloudStructures;
using CloudStructures.Structures;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace redisTest
{
    public class Redis
    {
        private RedisConnection _connection;

        public Redis()
        {
            var config = new RedisConfig("default", "127.0.0.1");
            _connection = new RedisConnection(config);
        }

        public async Task<bool> CheckAccountAsync(string userID)
        {
            try
            {
                RedisString<String> redisString = new(_connection, "test", null);
                var result = await redisString.SetAsync(userID);

                //result 에 따라 무엇이든 하겠지?.. 

                return true;
            }
            catch(Exception ex)
            {
                await Console.Out.WriteLineAsync(ex.Message);
                return false;
            }
        }

    }
}

````