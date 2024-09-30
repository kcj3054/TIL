## 타입변환

- 타입변환! c언어에서는 ()로 하면 타입이 변환이된다 그러나 c++에서는 이 넓은 c형식에서 세분화된 방식이 존재한다.!

- staic_cast, dynamic_cast, const_cast, reinterpret_cast가 존재한다!


## staic_cast


- 일반적인 타입변환이나, 부모 자식 사이에서 변환이 가능하도록한다고 보면된다.

## dynamic_cast<>()

- static_cast가 유사한데 반환형으로 만약 타입이 일치하지 않을 경우 nullptr을 반환한다! 

## const_cast<>()

- const가 필요하거나 필요하지않을 경우 붙여주기 ?, 삭제하기 용도로 사용이된다.!

- 일반적인 문자열에서 -> char *로 갈 경우 사용이된다
## reinterpret<>()

- 전혀 타입이 상관없는 메모리끼리의 변환이 가능하도록 한다!, void*는 타입이 없기에 여기에서 사용이 가능하다!

## 소스 

````c++
#include <iostream>
#include <vector>

using namespace std;

// 캐스팅!
//static_cast
//dynamic_cast
//const_cast
//reinterpret_cast

class Player
{
public:
	virtual ~Player() {}
};

class Knight : public Player
{
public:

};

class Archer : public Player
{
public:

};

class Dog
{

};
void PrintName(char* name)
{

}
int main()
{
	//static_cast<>: 누가 봐도 가능한 경우 캐스팅이된다. 1) int < - > float, 2) Player* - > Knight*(다운 캐스팅)
	// 다운캐스팅을 할 경우 안전성은 보장하지 못한다 

	int hp = 100;
	int maxHp = 200;
	float ratio = static_cast<float>(hp) / maxHp;

	Player* p = new Knight();
	Knight* k1 = static_cast<Knight*>(p);

	//RTTI (Runtime Type Information)
	//다형성을 활용하는 방식 
	//다형성을 활용하는 방식이니 가상함수가 필요하다, 가상함수는 virtual table을 이용해서 런타임에 이동해야할 주소를 가리켜
	//주기때문이다
	//dynamic_cast<>()를 사용하면, 장점이 머냐하면 만약 ()안의 타입 변환을 원하는 타입이 타입이 잘못되었을 경우
	//nullptr을 반환한다.
	//만약 Plyaer* p = new Archer();이라고 생각을 하면, nullptr을 반환하게된다.
	//장점이 있지만 static_cast<>()에 비해 느리다
	Knight* k2 = dynamic_cast<Knight*>(p);

	//const_cast<>()
	//PrintName("kcj3054");   <- 의 경우 오류가난다 왜냐하면 kcj3054는 const형이라서.. 그래서 그것을 떼거나 붙이기 위해서
	//const_cast<>()가 쓰인다
	PrintName(const_cast<char*>("kcj3054"));

	//re-interpret
	//다시 - 간주하다
	//reinterpret_cast
	//포인터랑 전혀 관계없는 다른 타입으로 변환 
	//__int64는 수이고, k2는 주소이다 전혀 상관없지만 reinterpret_cast로는 가능하다.

	__int64 address = reinterpret_cast<__int64>(k2);

	//전혀 상관없는 클래스끼리도 가능! 
	Dog* dog1 = reinterpret_cast<Dog*>(k2);

	//malloc의 경우 반환형이 void*였다.!
	void* p = malloc(1000);

	Dog* dog2 = reinterpret_cast<Dog*>(p);
	return 0;
}
````