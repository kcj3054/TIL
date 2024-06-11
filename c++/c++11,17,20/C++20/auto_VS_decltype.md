# auto, decltype

```c++

#include <iostream>
#include <vector>
#include <string_view>

using namespace std;

template<typename T>
constexpr string_view getTypeName()
{
	if constexpr (std::is_same_v<T, int>)
		return "int";
	else if constexpr (std::is_same_v<T, int&&>)  // c++ 17부터 도입된 기능 is_same_v<>
		return "int&&";
	else if constexpr (std::is_same_v<T, int&>)
		return "int&";
	else
		return "unknown type";
}

template<typename T>
void printType(T&& t)  // std::move로 전달하지 않으면 이부분에서 int&& -> int&로 된다. 
{
	// Decltype to get the exact type of t
	cout << getTypeName<decltype(t)>() << endl;

}

void ex5()
{
	//visual studio에서 디버깅 시 형식이 나오네 

	int i = 42;
	auto&& ri_1 = i; // i는 l-value이므로 ri_1는 int& 타입이 됩니다.
	// cout << "ri_1 type : " << typeid(ri_1).name() << endl;

	auto&& ri_2 = 42; // 42는 r-value이므로 ri_2는 int&& 타입이 됩니다.
	// cout << "ri_2 type : " << typeid(ri_2).name() << endl
	cout << "ri_1 type : ";
	printType(ri_1);

	cout << "ri_2 type : ";  // 여기서 디버깅 시 int&&로 잡힘 d
	// printType(ri_2);  // 여기서도 int&로 나와 ..
	
	/*
	* ri_2는 int&& 타입이지만, 변수로 사용될 때는 l-value입니다. 이는 모든 이름이 붙은 변수가 l-value로 간주된다는 의미입니다.
	*/
	printType(ri_2);
	// printType(std::move(ri_2));
}

template<typename T, typename S>
void func_ex7(T lhs, S rhs)
{
	auto prod1 = lhs * rhs;

	//decltype 값을 받아서 컴파일 타임에 타입을 추론한다 
	typedef decltype(lhs* rhs) product_type; // decltype은 계산을 하지 않고 추론까지한다 
	product_type prod2 = lhs * rhs;

	//decltype(lhs * rhs) prod3 = lhs * rhs
	// decltype prod3 = lhs * rhs
}

//decltype auto와 다르다.. 선언이 된 타입을 그대로 가져온다. 
// trailing return type.. -> auto키워드로 정의된 함수의 반환형을 명시적으로 알려줌.
template<typename T, typename S>
auto func_ex8(T lhs, S rhs) -> decltype(lhs* rhs)
{
	return lhs * rhs;
}



template<typename T, typename S>
auto fmin_test(T x, S y)
{
	return x < y ? x : y;
}


int main()
{
	// ex5();
	auto res2 = fmin_test(2.2, 1);


	// auto b; // 안됌 -> auto는 초기값 할당이 필요함 (컴파일 시 추론)

	//auto res = func_ex8(2, 2.2);
	//cout << res << endl;

	//{
	//	std::vector<int> vect = { 42,  43 };

	//	auto first_element = vect[0]; // first_element가 int로
	//	decltype(vect[1]) second_element = vect[1]; // int& 왜 vec[]의 return type이 &라서.
	//}


	//lambda에서 반환 명시할 때 trailing return type을 사용해야함 
	[](int* p) -> int& {return *p;}; // ok
	// int& [](int* p) {return *p;}; // nope

	//class member function에서 return 타입 명시할 때도 trailing return type을 사용하면 훨씬 간결하다는 글도 존재한다 




	return 0;
}

```
