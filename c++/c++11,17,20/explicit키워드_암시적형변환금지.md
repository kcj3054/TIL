## explicit 키워드 

- 암시적 형 변화이란?
  - 컴파일러가 자동으로 한 타입의 값을 다른 타입의 값으로 변환해주는 것을 의미합니다.

- 아래 예제에서 컴파일러는 암시적으로 형 변환을 해서 int 타입의 10을 MyClass 타입으로 변환해주는 것이다.....즉 즉  MyClass obj = 10이 -> MyClass obj = MyClass(10); 와 동일하도록 변환해주는 것이다. 
  -  MyClass obj = 10; // 암시적 형 변환이 발생함 , 생성자에 explicit 키워드를 붙이면 컴파일 에러가 발생함 

````c++


class MyClass
{
public:
	//암시적 형 변환이 가능한 생성자 
	explicit MyClass(int value) : _value(value) { std::cout << "myclass 생성자 호출 됌" << std::endl; }

	void display() const
	{
		std::cout << "Value : " << _value << std::endl;
	}
private:
	int _value;
};



int main()
{
	// MyClass obj = 10; // 암시적 형 변환이 발생함 , 생성자에 explicit 키워드를 붙이면 컴파일 에러가 발생함 
	
	// MyClass obj = MyClass(10);

	// MyClass obj(10); // 명시적으로 생성자를 호출 함 

	// obj.display();
}

````


- 위의 이유로 일반적인 상황에서는 암시적 형변환이 일어나는 것을 허용하지 않는다 그러므로 클래스의 생성자쪽에서는 explicit 키워드를 꼭 붙여서 암시적으로 형 변환되는 것을 막도록하자. 