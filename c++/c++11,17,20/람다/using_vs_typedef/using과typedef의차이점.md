## using이 먼가요 ??

- using 문법은 c++11에 나온 모던c++ 문법이다.

- using 과 typedef 둘다 별칭을 지어서 사용한다는 점이 존재한다.



## typedef의 예시 단점.

- typedef은 템플릿과 같이 사용하지 못한다.  그렇지만 struct를 같이 사용하면 될 수는 있다.

#### 예시  (안되는 예시)

````
template<typename T>
typedef vector<T> List;
````


#### 구조체와 함께 사용한 예시 (구조체안에 typedef를 넣으면 템플릿과 같이 사용가능하다)

````
template<typename T>
struct List2
{
    typedef list<T> type;
}
````


- 직관적이지않다 using을 사용한다면 함수포인터 같은 것을 직관적으로 읽기 쉬운데 typedef는 그렇지않다



````
//using 버전
using FunctPointer1 = void(*)();

//typedef 버전
typedef void(*FunctPointer2)();
````




## 소스 + 주석

````
#include <bits/stdc++.h>
using namespace std;

//using vs typedef


typedef vector<int>::iterator VectorIt;

typedef int id;
using id = int;


//using 문법이 더 직관적이다. 첫번째 함수포인터는 직관적이지않은데 using을 사용하면 조금 더 직관적이다.
typedef void(*FuncPointer)();
using FuncPointer2 = void(*)();

//using은 템플릿이 적용이 되는데 typedef는 안된다.
template<typename T>
using List = vector<T>;

template<typename T>
struct List2
{
   typedef list<T> type;
};

int main()
{
   id studentId = 0;


   List<int> li;
   li.push_back(1);
   li.push_back(2);

   List2<int>::type li2;
   li2.push_back(1);

}
````