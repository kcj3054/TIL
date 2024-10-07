### RVO

- RVO란? RETURN VALUE OPTIMIZED이다. 

- 리턴 값을 왜 ? 최적화 하냐? 
    > 일반적으로 c++은 call by value이다 이럴 때 복사가 생기면서 메모리적인 단점이 발생하는데 그러하는 부분들을 해결하기 위해서 call by refrence..나 return value optimized가 존재한다.

    > rvo는 c++ 17로 오면서 강제되었다고한다. 일반적으로 임시 객체가 생성될 때 생성되지 않게 compiler가 최적화를 보장해주는 것이다 아래의 코드에 예시가 존재한다.


````c++
std::string bar()
{
    return std::string("hello");
}
````

- 위의 문장은 일반적으로 임시 객체가 생성되어야한다. 
- hello 부분에서 임시 객체가 생성되고  임시객체를 호출자에게 반환하고, 임시객체를 소멸한다 
- 정말 쓸모 없는 일을 하고있는 것이다. 

- rvo가 적용된다면 임시 객체의 생성과 복사가 생략된다, 함수 bar가 반환하는 것이 호출자에게 직접 생성되는 것이다. 

````
숨겨진 코드이다.
std::string temp = std::string("hello"); // 임시 객체 생성
return temp; // 

RVO 적용 
// 임시 객체 없이 직접 생성
return std::string("hello");
````


#### 예제 코드 

````
#include <iostream>
#include <string>

std::string bar() {
    return std::string("hello");
}

int main() {
    std::string result = bar();
    std::cout << result << std::endl;
    return 0;
}
````

- 컴파일러 옵션을 키고 끄면서 최적화 된 모습을 확인 할 수 있다. 
