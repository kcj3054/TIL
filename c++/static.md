
## static?

- struct와 class의 차이
    - struct는 기본적으로 public 접근제한자인데, class는 기본적으로 private 접근제한자이다.
- static(정적, 고정된) 
- 모든 마린이 공통적으로 공격이 있는데, a마린과 b마린의 공격력이 다르면 안된다. 
static을 사용하면 특정 객체에 해당하는 것이 아니라 마린이라는 class에 연관지을 수 있다! 

````
#include <bits/stdc++.h>

using namespace std;


class Marine
{

public:
	int _hp;

	static void SetAttack() {}


	static int s_attack; // 
};
int main() {

	Marine m1;

	Marine::s_attack = 10;
	Marine::SetAttack();
	return 0;
}

````


## 클래스 내부의 static변수 초기화 관련 내용

### 잘못된 초기화 

- 클래스 내부의 static 변수는 별도의 공간(data 영역)에 잡히게된다. 그래서 한번만 초기화 되고, 클래스 내의 정적 변수는 객체가 공유한다.  이러한 이유로 정적 변수의 복사본이 여러개 있을 수는 없다.!!
````
#include<iostream>
using namespace std;
  
class GfG
{
   public:
     static int i;
      
     GfG()
     {
        // Do nothing
     };
};
  
int main()
{
  GfG obj1;
  GfG obj2;
  obj1.i =2;
  obj2.i = 3;
    
  // prints value of i
  cout << obj1.i<<" "<<obj2.i;   
}
````

### 바른 초기화
-  클래스 내부의 정적변수는 클래스 외부의 클래스이름 및 범위확인 연산자를 사용하여 명시적으로 초기화해야한다.
````
#include<iostream>
using namespace std;
  
class GfG
{
public:
    static int i;
      
    GfG()
    {
        // Do nothing
    };
};
  
int GfG::i = 1;
  
int main()
{
    GfG obj;
    // prints value of i
    cout << obj.i; 
}
````
-출처 : https://www.geeksforgeeks.org/static-keyword-cpp/