## delete (C++ 11)

- delete? 내가 필요로하지 않는 함수를 삭제하는 것이다. ! 

- c++11에 delete가 나오기 전에는 private를 이용해서 사용하지 않을 함수를 막을 수 있었다 그렇지만 여기서 private로 하더라도 friend를 이용하면 프렌드인 클래스는 접근이 가능하다.. 이건 반쪽짜리 막기 방법이다. 여기서 완전히 막는 방법이 delete로 나오게 되었다.


## 복사 대입연산자 막기 private 버전 

````
#include <iostream>
using namespace std;

class Knight
{
public:
private:
    void operator=(const Knight& k1)
    {

    }

    //friend class Admin; 
private:
    int _hp = 100;
};

class Admin
{
public:
    void CopyKnight(const Knight& k)
    {
        Knight k1;
        k1 = k;
    }
};
````

- 위 코드에서 private 내부에 주석 처리된 friend class Admin을 해제하면 Admin 클래스에서는 Knight의 복사 연산자가 허용이된다.. 이렇게 되면 무용지물이되는 것이다..

- 이 반쪽짜리 막기를 해결하기 위해서 나온 것이 delete 버전! 

## c++11 delete 함수 

````
#include <iostream>

using namespace std;

class Knight
{
public:
   
public:
    void operator=(const Knight&) = delete; 
private:
    int _hp = 100;
};
````

- 간단하다 ! public으로 열어주되 사용하지 않을 함수를 = delete로 막아주면 끝..