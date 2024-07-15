## 캐스팅에 관하여...

- 캐스팅에는 static_cast, const_cast<>(), dynamic_cast<>()..가 있다.

- static_cast<>()는 누가봐도 될 것같으면 가능하다, 타입변환이나 다운캐스팅.

- dynamic_cast<>()는 상속 관계에서의 안전한 형 변환이다. 

    - RTTI 다형성을 활용하는 방식, virtual함수를 하나라도 만들었으면 객체 메모리에 가상함수 테이블 주소가 기입된다. dynamic_cast를 사용했을 때 잘못된 타입으로 캐스팅을 하면 nullptr이 반환되어서 타입이 맞는지 확인할 때유용하다.





## 소스
````
#include <bits/stdc++.h>

using namespace std;

/*
캐스팅의 종류
1) static_cast
2) dynamic_cast
3) const_cast
4) reinterpret_cast
*/

class Player
{
public:
	virtual ~Player(){}
};

class Knight : public Player
{

};
class Archer : public Player
{

};

void PrintName(char * Name)
{

}
int main()
{
	//static_cast : 타입 원칙에 비춰볼때 누가봐도 가능한 경우일때만 가능하다. 
	/*
	1) int < - > float
	2) Player * - > Knight*(다운캐스팅) 
	*/

	int hp = 100;
	int maxHp = 200;
	float ratio = static_cast<float> (hp) / maxHp;  // 실수연산이 우선순위가 높아서 float로 변환된다 

	// 부모에서 자식으로 
	Player * p = new Knight();
	Knight * k1 = (Knight*)p;

	//dynamic_cast : 상속 관계에서의 안전한 형 변환 
	/*
	RTTI(RunTime Type Information)
	-다형성을 활용하는 방식 
	virtual함수를 하나라도 만들면, 객체 메모리에 가상 함수 테이블 주소가 기입된다.
	잘못된 타입으로 캐스팅 했으면 nullptr반환
	*/
	Knight* k2 = dynamic_cast<Knight*> (p); // p가 원래 Knight*타입이 아니면 k2를 nullptr로 반환된다 주로 맞는 타입으로 캐스팅 했는지 확인에 유용.

	//PrintName에는 char *,  kcj3054는 const char *따라서 kcj3054를 넘기면 오류가 발생 
	PrintName(const_cast<char*>("kcj3054"));
	return 0;
}
````


### reinterpret_cast vs static_cast

- static_cast 안정적인 타입이나 연관관계가 있는 포인터끼리는 형 변환을 허용한다. 
	- 예를들어 상속관계에 있는 형변환은 가능하다 
	- 그렇지만 전혀관계없는 포인터끼리의 형 변환은 불가능하다


- reinterpret_cast는 모든 타입을 강제로 형변환이 가능하다 그렇지만 메모리 배열들을 강제려 변환시키는 것이라서 문제가 발생할 수도있고 실무에서는 성능 문제로 reinterpret_cast를 잘 사용하지않으려고한다. 그렇지만 부하테스트를 한 후에도 큰 변화가 없다면 reinterpret_cast를 사용하기도한다.

````c++
#include <iostream>



class Base
{
public:
	virtual void show() { std::cout << "Base\n" << std::endl; }
};

class Derived : public Base
{
public:
	virtual void show() { std::cout << "Derived\n" << std::endl; }
};

class Unrelated
{
public:
	void show() { std::cout << "Unrelated\n" << std::endl; }

};

int main()
{
	Base* base = new Base();
	Derived* derived = new Derived();
	Unrelated* unrelated = new Unrelated();

	//static_cast 안전한 타입 변환 
	// upcast
	auto baseFromDerived = static_cast<Base*>(derived);

	// reinterpret 
	//특히, 변환된 포인터를 통해 원래 객체의 메서드를 호출하려고 할 때, 
	//객체의 메모리 레이아웃이 일치하지 않으면 정의되지 않은 동작이 발생할 수 있습니다.
	//Base의 vtable(가상 함수 테이블)이나 다른 내부 구조를 참조하려고 할 때 예기치 않은 결과가 발생합니다.
	auto unrelatedFromBase = reinterpret_cast<Base*>(unrelated);

	// C++에서 가상 함수의 동작 방식 때문입니다. 
	// C++에서 가상 함수는 런타임에 동적 바인딩(dynamic binding)을 통해 호출되므로, 
	// 포인터 타입이 변환되더라도 실제 객체의 타입에 따라 적절한 함수가 호출됩니다.
	baseFromDerived->show();

	unrelatedFromBase->show();

	//안되는 case static_cast로 다른 포인터 형변환 
	// auto baseFromDerived = static_cast<Unrelated*>(derived); -> 컴파일 조차안된다.
	auto baseFromDerived = reinterpret_cast<Unrelated*>(derived); // 컴파일 가능하다

	return 0;
}
````