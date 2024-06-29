## redis 

- c++에서는 redis를 사용할 때 2가지 방안이 존재한다 redis plus plus, hredis. 두가지 모두 살펴보았는데 조금 더 사용하기 쉬운 것은 redis plus plus이다 

### HiREDIS

- 장점
    - 경량 및 빠른 속도
    - c기반으로 간단하게 사용할 수 있음
- 단점
    - 고수준의 기능이나 개체지향적인 인터페이스는 부족함
    - 멀티스레드 지원이 부족함


### Redis++

- 내부적으로는 hiredis를 사용 함
- 고수준의 기능 제공 
- 멀티스레드에 안전 
- hredis에 비해 약간의 오버헤드가 있을 수 있음 

````c++
#include <sw/redis++/redis++.h>
#include <iostream>

using namespace sw::redis;

int main() {
    try {
        auto redis = Redis("tcp://127.0.0.1:6379");

        redis.set("key", "value");  // test 용도 
        
        auto val = redis.get("key");
        if (val) {
            std::cout << "key: " << *val << std::endl;
        } else {
            std::cout << "key does not exist" << std::endl;
        }

        redis.ping(); // 연결 상태 확인을 위한 ping

    } catch (const Error &e) {
        std::cerr << "Redis error: " << e.what() << std::endl;
    }

    return 0;
}

````

- redis++ 설치
    - vcpkg를 이용하여 설치 
````
git clone https://github.com/microsoft/vcpkg.git
cd vcpkg
./bootstrap-vcpkg.sh

````

- .\vcpkg.exe integrate install

- ./vcpkg install hiredis

- 사용 가능